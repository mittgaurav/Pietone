import numpy as np
from neural_network import OneLayerNN

def scaled_dot_product_attention(Q, K, V, mask=None):
    """Compute scaled dot-product attention
    Optional mask to apply to the scores"""
    d_k = Q.shape[-1]
    scores = np.matmul(Q, K.transpose(0, 1, 3, 2))
    scores /= np.sqrt(d_k)

    if mask is not None:
        scores += mask

    weights = np.exp(scores - np.max(scores, axis=-1, keepdims=True))
    weights /= np.sum(weights, axis=-1, keepdims=True)

    output = np.matmul(weights, V)
    return output

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

def layer_normalization(x, epsilon=1e-6):
    """Apply layer normalization to stabilize training."""
    mean = np.mean(x, axis=-1, keepdims=True)
    variance = np.var(x, axis=-1, keepdims=True)
    normalized = (x - mean) / np.sqrt(variance + epsilon)
    return normalized


class MultiHeadAttention:
    """Multi-Head Attention mechanism.
    Allows the model to attend to different parts of the input
    sequence simultaneously by using multiple attention heads,
    each focusing on a different aspects of the sequence"""
    def __init__(self, d_model, num_heads):
        self.d_model = d_model             # Dimensionality of model embeddings
        self.num_heads = num_heads         # Number of parallel attention heads
        self.depth = d_model // num_heads  # Depth of each attention head

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
        V: Value matrix, sequence values containing context
        """
        Q = np.matmul(Q, self.Wq)
        K = np.matmul(K, self.Wk)
        V = np.matmul(V, self.Wv)

        Q = self.split_heads(Q)
        K = self.split_heads(K)
        V = self.split_heads(V)

        attention_output = scaled_dot_product_attention(Q, K, V)
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

        self.Wo -= learning_rate * np.matmul(self.output.T, d_output)
        self.Wq -= learning_rate * np.matmul(self.Q.T, dQ)
        self.Wk -= learning_rate * np.matmul(self.K.T, dK)
        self.Wv -= learning_rate * np.matmul(self.V.T, dV)

        return dQ, dK, dV


class Transformer:
    """Transformer model with multi-head attention and feed-forward network"""
    def __init__(self, d_model, num_heads, num_layers, d_ff, max_len=1000, learning_rate=0.01):
        self.d_model = d_model             # Dimensionality of the model
        self.num_heads = num_heads         # Number of attention heads
        self.num_layers = num_layers       # Number of transformer layers
        self.d_ff = d_model                # Feed-forward network dimension
        self.learning_rate = learning_rate
        self.positional_encodings = self.get_positional_encoding(max_len, d_model)
        self.layers = [self.build_layer() for _ in range(num_layers)]

    def get_positional_encoding(self, max_len, d_model):
        """Generate positional encodings."""
        position = np.arange(max_len)[:, np.newaxis]
        div_term = np.exp(np.arange(0, d_model, 2) * -(np.log(10000.0) / d_model))
        pe = np.zeros((max_len, d_model))
        pe[:, 0::2] = np.sin(position * div_term)
        pe[:, 1::2] = np.cos(position * div_term)
        return pe

    def build_layer(self):
        """Build a single Transformer layer."""
        return {
            'attention': MultiHeadAttention(self.d_model, self.num_heads),
            'feed_forward': OneLayerNN(self.d_model, self.d_model)
        }

    def forward(self, x):
        """Forward pass through the Transformer model."""
        seq_len = x.shape[1]
        x = x.astype(float)
        x += self.positional_encodings[:seq_len]  # Add positional encoding

        activations = []
        for layer in self.layers:
            # Multi-head attention
            # We want to see how each word relates to every word
            # Thus we provide the input sequence for Q, K, and V
            attention_output = layer['attention'].forward(x, x, x)
            x = layer_normalization(x + attention_output)  # Add & Norm
            activations.append(x.copy())

            # Feed-forward network
            ff_output = layer['feed_forward'].forward(x)
            x = layer_normalization(x + ff_output)  # Add & Norm

        return x, activations

    def backward(self, X, y_true, y_pred, activations):
        """Backward pass through the Transformer model."""
        # Backward pass through each layer
        for i in reversed(range(self.num_layers)):
            layer = self.layers[i]
            # Backward pass for feed-forward network
            dW, _ = layer['feed_forward'].backward(activations[i], y_pred, y_true)

            # Backward pass for multi-head attention
            return layer['attention'].backward(dW)

    def train(self, X_train, y_train, epochs):
        """Train network using forward and backward prop"""
        for epoch in range(epochs):
            # Forward pass: Calculate predicted y
            y_pred, activations = self.forward(X_train)
            # Backward pass: Update weights
            self.backward(X_train, y_pred, y_train, activations)

            if epoch % (epochs // 10) == 0 or epoch == epochs - 1:
                print(f'Epoch {epoch}, Loss: {np.mean((y_pred - y_train) ** 2):.4f}')


# Example data: simple phrases and their reversed versions
phrases = ["hello world", "goodbye moon", "transformer model"]
reversed_phrases = [phrase[::-1] for phrase in phrases]

def tokenize(phrases):
    words = set(word for phrase in phrases for word in phrase.split())
    word_to_index = {word: i + 1 for i, word in enumerate(words)}
    index_to_word = {i: word for word, i in word_to_index.items()}
    return word_to_index, index_to_word

def to_numpy_arrays(phrases, reversed_phrases, word_to_index, max_len):
    X = np.zeros((len(phrases), max_len), dtype=int)
    y = np.zeros((len(reversed_phrases), max_len), dtype=int)

    for i, phrase in enumerate(phrases):
        seq = [word_to_index.get(word, 0) for word in phrase.split()]
        X[i, :len(seq)] = seq

    for i, reversed_phrase in enumerate(reversed_phrases):
        seq = [word_to_index.get(word, 0) for word in reversed_phrase.split()]
        y[i, :len(seq)] = seq

    return X, y

# Initialize tokenizers
word_to_index, index_to_word = tokenize(phrases)

# Define maximum length of sequences
max_len = max(max(len(p.split()) for p in phrases), max(len(p.split()) for p in reversed_phrases))

# Convert to numpy arrays
X_train, y_train = to_numpy_arrays(phrases, reversed_phrases, word_to_index, max_len)


# Define hyperparameters
d_model = 512
num_heads = 8
num_layers = 2
d_ff = 512
learning_rate = 0.01
epochs = 20

# Initialize Transformer model
transformer = Transformer(d_model=d_model, num_heads=num_heads, num_layers=num_layers, d_ff=d_ff, max_len=max_len)

# Training the model
transformer.train(X_train, y_train, epochs=epochs)

def reverse_phrase(phrase):
    """Reverse a phrase using the trained Transformer model."""
    # Tokenize and pad the input phrase
    sequence = [word_to_index.get(word, 0) for word in phrase.split()]  # Use 0 for unknown words
    sequence_padded = np.zeros((1, max_len), dtype=int)
    sequence_padded[0, :len(sequence)] = sequence

    # Perform forward pass
    output = transformer.forward(sequence_padded)[0]

    # Convert model output to indices
    reversed_indices = np.argmax(output, axis=-1)[0]

    # Convert indices to words
    reversed_words = [index_to_word.get(idx, '') for idx in reversed_indices if idx != 0]

    return ' '.join(reversed_words).strip()

# Test the model
test_phrases = ["hello world", "goodbye moon", "transformer model"]

# Display results
for test_phrase in test_phrases:
    reversed_output = reverse_phrase(test_phrase)
    print(f"Original: {test_phrase}")
    print(f"Reversed: {reversed_output}")
    print()
