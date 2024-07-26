"""
Neural Network with one, two, and any
number of layers.

Any non-use use of this code will be
dealt with fullest extent of the law.

@author: gaurav
"""
import numpy as np

def rms(y_pred, y_true):
    """Root mean squared error"""
    return np.mean((y_pred - y_true) ** 2)

def rms_deriv(y_pred, y_true):
    """RMS error derivative"""
    return 2 * (y_pred - y_true) / len(y_pred)

def relu(X):
    """ReLU activation function"""
    return np.maximum(0, X)

def relu_deriv(X):
    """Derivative of the ReLU"""
    return np.where(X > 0, 1, 0)

class OneLayerNN:
    """Single layer perceptron"""
    def __init__(self, input_size, output_size, learning_rate=0.01):
        self.input_size = input_size
        self.output_size = output_size
        self.learning_rate = learning_rate

        # Initialize weights and biases for the network
        self.W = np.random.randn(input_size, output_size) # Weight matrix
        self.b = np.zeros((1, output_size))               # Bias vector

    def forward(self, X):
        """Forward propagation through the network"""
        return np.dot(X, self.W) + self.b

    def backward(self, X, y_pred, y_true):
        """Backpropagate through the network
        Calculates the gradient of loss with
        respect to the weights and biases"""
        dE = rms_deriv(y_pred, y_true)
        dW = np.dot(X.T, dE)
        db = np.sum(dE, axis=0, keepdims=True)

        # Update the weights and biases using gradient descent
        self.W -= self.learning_rate * dW
        self.b -= self.learning_rate * db

    def train(self, X_train, y_train, epochs):
        """Train network using forward and backward prop"""
        for epoch in range(epochs):
            # Forward pass: Calculate predicted y
            y_pred = self.forward(X_train)
            # Backward pass: Update weights
            self.backward(X_train, y_pred, y_train)

            if epoch % (epochs // 10) == 0 or epoch == epochs - 1:
                print(f'Epoch {epoch}, Loss: {rms(y_pred, y_train):.4f}')

    def predict(self, X):
        """Predict on new data"""
        return self.forward(X)

class TwoLayerNN:
    """Two layer neural network"""
    def __init__(self, input_size, layer_size, output_size, learning_rate=0.01):
        self.input_size = input_size
        self.layer_size = layer_size
        self.output_size = output_size
        self.learning_rate = learning_rate

        # Initialize weights and biases for the network
        # He initialization
        self.W1 = np.random.randn(input_size, layer_size) * np.sqrt(2. / input_size)  # Weight matrix (1st)
        self.b1 = np.zeros((1, layer_size))  # Bias vector (1st)
        self.W2 = np.random.randn(layer_size, output_size) * np.sqrt(2. / layer_size) # Weight matrix (2nd)
        self.b2 = np.zeros((1, output_size))  # Bias vector (2nd)

    def forward(self, X):
        """Forward propagation through the network"""
        # Z1 = W1.X + b1
        Z1 = np.dot(X, self.W1) + self.b1
        # A1 = relu(Z1)
        A1 = relu(Z1)
        # y = W2.A1 + b2
        return A1, Z1, np.dot(A1, self.W2) + self.b2

    def backward(self, X, A1, Z1, y_pred, y_true):
        """Backpropagate through the network"""
        # E = (y - y0) ^ 2 / N
        # dE/dy = 2 * (y - y0)
        dE = rms_deriv(y_pred, y_true)

        # activation of output layer has no relu
        # dE/dW2 = dE/dy * dy/dW2
        # given y = W2.A1 + b2 => dy/dW2 = A1
        # so, dE/dW2 = dE/dy * A1
        dW2 = np.dot(A1.T, dE)
        db2 = np.sum(dE, axis=0, keepdims=True)

        # dE/dA1 = dE/dy * W2
        dA1 = np.dot(dE, self.W2.T)
        # dE/dZ1 = dE/dA1 * dA1/dZ1
        # given A1 = relu(Z1) => dA1/dZ1 = drelu
        # so, dE/Z1 = dE/dA1 * dr
        dZ1 = dA1 * relu_deriv(Z1)

        # dE/dW1 = dE/dZ1 * dZ1/dW1
        # given Z1 = W1.X + b1 => dZ1/dW1 = X
        # so, dE/W1 = dE/dZ1 * X
        dW1 = np.dot(X.T, dZ1)
        db1 = np.sum(dZ1, axis=0, keepdims=True)

        # Update the weights and biases using gradient descent
        self.W1 -= self.learning_rate * dW1
        self.b1 -= self.learning_rate * db1
        self.W2 -= self.learning_rate * dW2
        self.b2 -= self.learning_rate * db2

    def train(self, X_train, y_train, epochs):
        """Train network using forward and backward prop"""
        for epoch in range(epochs):
            A1, Z1, y_pred = self.forward(X_train)
            self.backward(X_train, A1, Z1, y_pred, y_train)

            if epoch % (epochs // 10) == 0 or epoch == epochs - 1:
                print(f'Epoch {epoch}, Loss: {rms(y_pred, y_train):.4f}')

    def predict(self, X):
        """Predict on new data"""
        _, __, y_pred = self.forward(X)
        return y_pred

class CustomLayerNN:
    """Custom number of layers in the network"""
    def __init__(self, input_size, layer_sizes, output_size, learning_rate=0.01):
        self.num_layers = len(layer_sizes) + 1
        self.learning_rate = learning_rate

        layers = [input_size] + layer_sizes + [output_size]
        self.W = [np.random.randn(layers[i], layers[i + 1]) * np.sqrt(2. / layers[i]) for i in range(len(layers) - 1)]
        self.b = [np.zeros((1, layers[i + 1])) for i in range(len(layers) - 1)]

    def forward(self, X):
        """Forward propagation through the network
        Calculate the output of all the layers and
        the last layer returns the final result"""
        A = X
        activations = [A]
        zctivations = []
        for i in range(self.num_layers):
            Z = np.dot(A, self.W[i]) + self.b[i]
            A = Z if i == self.num_layers - 1 else relu(Z)
            activations.append(A)
            zctivations.append(Z)
        return activations, zctivations

    def backward(self, activations, zctivations, y_true):
        """Backpropagate through the network
        Calculates the gradient of loss with respect to
        weights and biases - change in error per change
        in the weights and biases in every layer"""
        dZ = rms_deriv(activations[-1], y_true)
        dW = []
        db = []
        for i in reversed(range(self.num_layers)):
            dW.insert(0, np.dot(activations[i].T, dZ))
            db.insert(0, np.sum(dZ, axis=0, keepdims=True))
            if i > 0:
                dA = np.dot(dZ, self.W[i].T)
                dZ = dA * relu_deriv(zctivations[i - 1])

        for i in range(self.num_layers):
            self.W[i] -= self.learning_rate * dW[i]
            self.b[i] -= self.learning_rate * db[i]

    def train(self, X_train, y_train, epochs):
        """Train network using forward and backward prop"""
        for epoch in range(epochs):
            activations, zctivations = self.forward(X_train)
            self.backward(activations, zctivations, y_train)

            if epoch % (epochs // 10) == 0 or epoch == epochs - 1:
                print(f'Epoch {epoch}, Loss: {rms(activations[-1], y_train):.4f}')

    def predict(self, X):
        """Predict on new data - last layer"""
        activations, _ = self.forward(X)
        return activations[-1]

def test():
    """Generate one, two, and n layer neural network"""
    # Generate some synthetic data for training
    X_train = np.random.rand(100, 2)  # 100 samples, 2 features
    y_train = 2 * X_train[:, :1] + X_train[:, 1:]  # True function: 2*x1 + x2
    y_train += np.random.rand(100, 1) / 20  # up to 5% noise in sample

    # prediction data
    X_test = np.array([[0.5, 0.2], [0.3, 0.7]])  # Test inputs
    y_exp = 2 * X_test[:, 0] + X_test[:, 1]

    input_size = 2
    output_size = 1

    # Create and train the neural network
    print("===================")
    print("==== One layer ====")
    nn = OneLayerNN(input_size, output_size, learning_rate=0.1)
    nn.train(X_train, y_train, epochs=1000)

    # Test the trained network
    y_pred = nn.predict(X_test)
    print('Expected:', y_exp, 'Result:', y_pred.flatten())

    print("===================")
    print("==== Two layer ====")
    layer_size = 3
    nn = TwoLayerNN(input_size, layer_size, output_size, learning_rate=0.1)
    nn.train(X_train, y_train, epochs=1000)

    y_pred = nn.predict(X_test)
    print('Expected:', y_exp, 'Result:', y_pred.flatten())

    print("===================")
    print("=== Few layers ====")
    layer_sizes_sizes = [[100, 100], [10, 10, 10, 10, 10, 10]]

    for layer_sizes in layer_sizes_sizes:
        nn = CustomLayerNN(input_size, layer_sizes, output_size, learning_rate=0.01)
        nn.train(X_train, y_train, epochs=2000)

        y_pred = nn.predict(X_test)
        print('Expected:', y_exp, 'Result:', y_pred.flatten())

if __name__ == "__main__":
    test()
