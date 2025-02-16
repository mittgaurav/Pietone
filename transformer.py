import numpy as np
from neural_network import OneLayerNN


def softmax(x):
    """softmax function"""
    e_x = np.exp(x - np.max(x, axis=-1, keepdims=True))
    return e_x / e_x.sum(axis=-1, keepdims=True)

def layer_norm(x, eps=1e-6):
    """Apply layer normalization to stabilize training"""
    mean = np.mean(x, axis=-1, keepdims=True)
    std = np.std(x, axis=-1, keepdims=True)
    return (x - mean) / (std + eps)

def positional_encoding(seq_len, d_model):
    pos = np.arange(seq_len)[:, np.newaxis]
    i = np.arange(d_model)[np.newaxis, :]
    angle_rates = 1 / np.power(10000, (2 * (i // 2)) / np.float32(d_model))
    angle_rads = pos * angle_rates
    angle_rads[:, 0::2] = np.sin(angle_rads[:, 0::2])
    angle_rads[:, 1::2] = np.cos(angle_rads[:, 1::2])
    return angle_rads

def scaled_dot_product_attention(q, k, v, mask=None):
    """Compute scaled dot-product attention
    Optional mask to apply to the scores"""
    matmul_qk = np.matmul(q, k.transpose((0, 1, 3, 2)))
    dk = k.shape[-1]
    scaled_attention_logits = matmul_qk / np.sqrt(dk)

    if mask is not None:
        scaled_attention_logits += (mask * -1e9)

    attention_weights = softmax(scaled_attention_logits)
    output = np.matmul(attention_weights, v)
    return output, attention_weights

def scaled_dot_product_attention_backward(d_output, Q, K, V):
    """Backward pass for scaled dot-product attention."""
    d_k = Q.shape[-1]
    scores = np.matmul(Q, K.transpose(0, 1, 3, 2))
    scores /= np.sqrt(d_k)

    # Compute gradients
    d_scores = np.matmul(d_output, V.transpose(0, 1, 3, 2))
    d_scores /= np.sqrt(d_k)
    d_weights = np.exp(scores - np.max(scores, axis=-1, keepdims=True))
    d_weights /= np.sum(d_weights, axis=-1, keepdims=True)
    d_weights -= d_weights * np.sum(d_weights * d_scores, axis=-1, keepdims=True)

    dV = np.matmul(d_weights, V)
    dK = np.matmul(d_weights.transpose(0, 1, 3, 2), Q)
    dQ = np.matmul(d_weights, K)

    return dQ, dK, dV

def create_padding_mask(seq):
    return (seq == 0).astype(np.float32)[:, np.newaxis, np.newaxis, :]

class MultiHeadAttention:
    """Multi-Head Attention mechanism.
    Allows the model to attend to different parts of the input
    sequence simultaneously by using multiple attention heads,
    each focusing on a different aspect of the sequence"""
    def __init__(self, d_model, num_heads, learning_rate=0.01):
        self.d_model = d_model             # Dimensionality of model embeddings
        self.num_heads = num_heads         # Number of parallel attention heads
        self.depth = d_model // num_heads  # Depth of each attention head
        self.learning_rate = learning_rate
        # Initialize weight for queries, keys, values, and output projection
        self.Wq = np.random.randn(d_model, d_model) * np.sqrt(2.0 / d_model)
        self.Wk = np.random.randn(d_model, d_model) * np.sqrt(2.0 / d_model)
        self.Wv = np.random.randn(d_model, d_model) * np.sqrt(2.0 / d_model)
        self.Wo = np.random.randn(d_model, d_model) * np.sqrt(2.0 / d_model)

    def split_heads(self, x):
        """Splits the last dimension into (num_heads, depth)
        Rearranges tensor to separate different attention heads"""
        x = x.reshape(x.shape[0], x.shape[1], self.num_heads, self.depth)
        return np.transpose(x, (0, 2, 1, 3))

    def forward(self, Q, K, V):
        """Forward pass multi-head attention
        Q: Query matrix, current input's vector to focus on
        K: Key matrix, entire sequence's to match the query
        V: Value matrix, sequence values containing context"""
        Q = np.matmul(Q, self.Wq)
        K = np.matmul(K, self.Wk)
        V = np.matmul(V, self.Wv)

        Q = self.split_heads(Q)
        K = self.split_heads(K)
        V = self.split_heads(V)

        attention_output, _ = scaled_dot_product_attention(Q, K, V)
        attention_output = np.transpose(attention_output, (0, 2, 1, 3)).reshape(attention_output.shape[0], -1, self.d_model)
        output = np.matmul(attention_output, self.Wo)
        return output

    def backward(self, d_output):
        """Compute gradients for multi-head attention."""
        # Compute gradients for Wo
        d_attention_output = np.matmul(d_output, self.Wo.T)
        d_attention_output = d_attention_output.reshape(self.Q.shape[0], self.num_heads, -1, self.depth)
        d_attention_output = np.transpose(d_attention_output, (0, 2, 1, 3))

        # Backward pass for scaled dot-product attention
        dQ, dK, dV = scaled_dot_product_attention_backward(d_attention_output, self.Q, self.K, self.V)

        # Compute gradients for Q, K, V
        dQ = np.matmul(dQ, self.Wq.T)
        dK = np.matmul(dK, self.Wk.T)
        dV = np.matmul(dV, self.Wv.T)

        self.Wo -= self.learning_rate * np.matmul(self.output.T, d_output)
        self.Wq -= self.learning_rate * np.matmul(self.Q.T, dQ)
        self.Wk -= self.learning_rate * np.matmul(self.K.T, dK)
        self.Wv -= self.learning_rate * np.matmul(self.V.T, dV)

        return dQ, dK, dV

class Dropout:
    def __init__(self, rate):
        self.rate = rate
        self.mask = None

    def forward(self, X, training=True):
        if not training:
            return X
        self.mask = np.random.rand(*X.shape) > self.rate
        return X * self.mask / (1.0 - self.rate)

    def backward(self, d_output):
        return d_output * self.mask / (1.0 - self.rate)

class EncoderLayer:
    def __init__(self, d_model, num_heads, d_ff, learning_rate=0.01):
        self.d_model = d_model
        self.num_heads = num_heads
        self.d_ff = d_ff
        self.learning_rate = learning_rate

        self.attention = MultiHeadAttention(d_model, num_heads, learning_rate)
        self.ffn = OneLayerNN(d_model, d_ff, learning_rate)
        self.dropout = Dropout(0.1)  # Adding dropout

    def forward(self, x):
        attn_output = self.attention.forward(x, x, x)
        attn_output = layer_norm(x + attn_output)
        attn_output = self.dropout.forward(attn_output)

        ffn_output = self.ffn.forward(attn_output)
        output = layer_norm(attn_output + ffn_output)
        output = self.dropout.forward(output)
        return output, attn_output, ffn_output

    def backward(self, d_output, attn_output, ffn_output):
        d_ffn_output = self.ffn.backward(ffn_output, d_output)
        d_attn_output, dQ, dK, dV = self.attention.backward(d_ffn_output)
        return d_attn_output

class DecoderLayer:
    def __init__(self, d_model, num_heads, d_ff, learning_rate=0.01):
        self.d_model = d_model
        self.num_heads = num_heads
        self.d_ff = d_ff
        self.learning_rate = learning_rate

        self.self_attention = MultiHeadAttention(d_model, num_heads, learning_rate)
        self.enc_dec_attention = MultiHeadAttention(d_model, num_heads, learning_rate)
        self.ffn = OneLayerNN(d_model, d_ff, learning_rate)
        self.dropout = Dropout(0.1)  # Adding dropout

    def forward(self, x, enc_output):
        self_attn_output = self.self_attention.forward(x, x, x)
        self_attn_output = layer_norm(x + self_attn_output)
        self_attn_output = self.dropout.forward(self_attn_output)

        enc_dec_attn_output = self.enc_dec_attention.forward(self_attn_output, enc_output, enc_output)
        enc_dec_attn_output = layer_norm(self_attn_output + enc_dec_attn_output)
        enc_dec_attn_output = self.dropout.forward(enc_dec_attn_output)

        ffn_output = self.ffn.forward(enc_dec_attn_output)
        output = layer_norm(enc_dec_attn_output + ffn_output)
        output = self.dropout.forward(output)
        return output, self_attn_output, enc_dec_attn_output, ffn_output

    def backward(self, d_output, self_attn_output, enc_dec_attn_output, ffn_output):
        d_ffn_output = self.ffn.backward(ffn_output, d_output)
        d_enc_dec_attn_output, dQ, dK, dV = self.enc_dec_attention.backward(d_ffn_output)
        d_self_attn_output, dQ, dK, dV = self.self_attention.backward(d_enc_dec_attn_output)
        return d_self_attn_output

class Encoder:
    """Encoder consisting of multiple EncoderLayers"""
    def __init__(self, num_layers, d_model, num_heads, d_ff, vocab_size, max_len, learning_rate=0.01):
        self.num_layers = num_layers
        self.d_model = d_model
        self.num_heads = num_heads
        self.d_ff = d_ff
        self.learning_rate = learning_rate

        self.embedding = OneLayerNN(vocab_size, d_model, learning_rate)
        self.pos_encoding = positional_encoding(max_len, d_model)
        self.layers = [EncoderLayer(d_model, num_heads, d_ff, learning_rate) for _ in range(num_layers)]
        self.dropout = Dropout(0.1)

    def forward(self, x):
        seq_len = x.shape[1]
        x = self.embedding.forward(x) + self.pos_encoding[:seq_len]
        x = self.dropout.forward(x)
        attentions, ffn_outputs = [], []
        for layer in self.layers:
            x, attn_output, ffn_output = layer.forward(x)
            attentions.append(attn_output)
            ffn_outputs.append(ffn_output)
        return x, attentions, ffn_outputs

    def backward(self, d_output, attentions, ffn_outputs):
        for i in reversed(range(self.num_layers)):
            d_output = self.layers[i].backward(d_output, attentions[i], ffn_outputs[i])
        return d_output

class Decoder:
    """Decoder consisting of multiple DecoderLayers"""
    def __init__(self, num_layers, d_model, num_heads, d_ff, vocab_size, max_len, learning_rate=0.01):
        self.num_layers = num_layers
        self.d_model = d_model
        self.num_heads = num_heads
        self.d_ff = d_ff
        self.learning_rate = learning_rate

        self.embedding = OneLayerNN(vocab_size, d_model, learning_rate)
        self.pos_encoding = positional_encoding(max_len, d_model)
        self.layers = [DecoderLayer(d_model, num_heads, d_ff, learning_rate) for _ in range(num_layers)]
        self.dropout = Dropout(0.1)

    def forward(self, x, enc_output):
        seq_len = x.shape[1]
        x = self.embedding.forward(x) + self.pos_encoding[:seq_len]
        x = self.dropout.forward(x)
        self_attentions, enc_dec_attentions, ffn_outputs = [], [], []
        for layer in self.layers:
            x, self_attn_output, enc_dec_attn_output, ffn_output = layer.forward(x, enc_output)
            self_attentions.append(self_attn_output)
            enc_dec_attentions.append(enc_dec_attn_output)
            ffn_outputs.append(ffn_output)
        return x, self_attentions, enc_dec_attentions, ffn_outputs

    def backward(self, d_output, self_attentions, enc_dec_attentions, ffn_outputs):
        for i in reversed(range(self.num_layers)):
            d_output = self.layers[i].backward(d_output, self_attentions[i], enc_dec_attentions[i], ffn_outputs[i])
        return d_output

class Transformer:
    """Transformer model containing Encoder and Decoder"""
    def __init__(self, enc_vocab_size, dec_vocab_size, num_layers, d_model, num_heads, d_ff, max_len, learning_rate=0.01):
        self.encoder = Encoder(num_layers, d_model, num_heads, d_ff, enc_vocab_size, max_len, learning_rate)
        self.decoder = Decoder(num_layers, d_model, num_heads, d_ff, dec_vocab_size, max_len, learning_rate)
        self.final_layer = OneLayerNN(d_model, dec_vocab_size, learning_rate)

    def forward(self, enc_inp, dec_inp):
        enc_output, enc_attns, enc_ffns = self.encoder.forward(enc_inp)
        dec_output, dec_self_attns, dec_enc_dec_attns, dec_ffns = self.decoder.forward(dec_inp, enc_output)
        final_output = self.final_layer.forward(dec_output)
        return final_output, enc_output, dec_output, enc_attns, enc_ffns, dec_self_attns, dec_enc_dec_attns, dec_ffns

    def backward(self, d_final_output, y_true, y_pred, enc_output, dec_output, enc_attns, enc_ffns, dec_self_attns, dec_enc_dec_attns, dec_ffns):
        d_dec_output = self.final_layer.backward(d_final_output.T, y_pred, y_true)
        d_enc_output = self.decoder.backward(d_dec_output, dec_self_attns, dec_enc_dec_attns, dec_ffns)
        self.encoder.backward(d_enc_output, enc_attns, enc_ffns)

    def train(self, X_train, y_train, epochs):
        for epoch in range(epochs):
            final_output, enc_output, dec_output, enc_attns, enc_ffns, dec_self_attns, dec_enc_dec_attns, dec_ffns = self.forward(X_train, y_train)
            d_final_output = 2 * (final_output - y_train) / y_train.size  # Gradient of the MSE loss w.r.t. final output
            self.backward(d_final_output, y_train, final_output, enc_output, dec_output, enc_attns, enc_ffns, dec_self_attns, dec_enc_dec_attns, dec_ffns)

            if epoch % (epochs // 10) == 0 or epoch == epochs - 1:
                print(f'Epoch {epoch}, Loss: {np.mean((final_output - y_train) ** 2):.4f}')

    def predict(self, X):
        dec_input = np.zeros((X.shape[0], X.shape[1], self.final_layer.output_size))  # Initialize decoder input with zeros
        final_output, _, _, _, _, _, _, _ = self.forward(X, dec_input)
        return np.argmax(final_output, axis=-1)  # Return the predicted indices

def one_hot_encode(sequence, vocab_size):
    return np.eye(vocab_size)[sequence]

def string_to_indices(s, char_to_index):
    return np.array([char_to_index[char] for char in s])

def indices_to_string(indices, index_to_char):
    return ''.join([index_to_char[index] for index in indices])

# Example strings
input_strings = ["hello", "world", "abcde"]
target_strings = [s[::-1] for s in input_strings]  # reverse word using tf

# Character to index mapping
chars = sorted(set(''.join(input_strings)))
char_to_index = {char: idx for idx, char in enumerate(chars)}
index_to_char = {idx: char for char, idx in char_to_index.items()}
vocab_size = len(chars)

# Prepare data
X_train = np.array([string_to_indices(s, char_to_index) for s in input_strings])
y_train = np.array([string_to_indices(s, char_to_index) for s in target_strings])

# One-hot encode the input and target sequences
X_train = one_hot_encode(X_train, vocab_size)
y_train = one_hot_encode(y_train, vocab_size)

# Transformer hyperparameters
num_layers = 2
d_model = 64
num_heads = 8
d_ff = 64
max_len = max(len(s) for s in input_strings)
learning_rate = 0.01
epochs = 1000

# Initialize and train transformer
transformer = Transformer(vocab_size, vocab_size, num_layers, d_model, num_heads, d_ff, max_len, learning_rate)
transformer.train(X_train, y_train, epochs)

# Predict
test_strings = ["hello", "world", "abcde"]
X_test = np.array([string_to_indices(s, char_to_index) for s in test_strings])
X_test = one_hot_encode(X_test, vocab_size)
predictions = transformer.predict(X_test)

# Convert predictions back to strings
predicted_strings = [indices_to_string(pred, index_to_char) for pred in predictions]
print(predicted_strings)  # Should print reversed strings
