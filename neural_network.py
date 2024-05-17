import numpy as np

class OneLayerNN:
    def __init__(self, input_size, output_size, learning_rate=0.01):
        self.input_size = input_size
        self.output_size = output_size
        self.learning_rate = learning_rate

        # Initialize weights and biases for the network
        self.W = np.random.randn(input_size, output_size)  # Weight matrix
        self.b = np.random.randn(1, output_size)           # Bias vector

    def forward(self, X):
        # Forward propagation through the network
        # Calculate the output (predicted values)
        return np.dot(X, self.W) + self.b

    def backward(self, X, y_pred, y_true):
        # Backpropagation through the network
        # Calculate the gradient of the loss with respect to the weights and biases
        error = (y_pred - y_true) / len(y_pred)
        dW = np.dot(X.T, error)
        db = np.sum(error, axis=0, keepdims=True)

        # Update the weights and biases using gradient descent
        self.W -= self.learning_rate * dW
        self.b -= self.learning_rate * db

    def train(self, X_train, y_train, epochs):
        # Train the network using forward and backward propagation
        for epoch in range(epochs):
            # Forward pass: Calculate predicted y
            y_pred = self.forward(X_train)

            # Backward pass: Update weights
            self.backward(X_train, y_pred, y_train)

            loss = np.mean((y_pred - y_train) ** 2)
            if epoch % 100 == 0 or epoch == epochs - 1:
                print(f'Epoch {epoch}, Loss: {loss:.4f}')

    def predict(self, X):
        # Make predictions on new data
        return self.forward(X)


class TwoLayerNN:
    def __init__(self, input_size, hidden_size, output_size, learning_rate=0.01):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.learning_rate = learning_rate

        # Initialize weights and biases for the network
        self.W1 = np.random.randn(input_size, hidden_size)  # Weight matrix for first layer
        self.b1 = np.random.randn(1, hidden_size)           # Bias vector for first layer
        self.W2 = np.random.randn(hidden_size, output_size) # Weight matrix for second layer
        self.b2 = np.random.randn(1, output_size)           # Bias vector for second layer

    def forward(self, X):
        # Forward propagation through the network
        # Calculate the output of the first layer
        # z1 = W1.X + b1
        self.z1 = np.dot(X, self.W1) + self.b1
        # a1 = relu(z1)
        self.a1 = self.relu(self.z1)

        # Calculate the output of the second layer
        # y = W2.a1 + b2
        return np.dot(self.a1, self.W2) + self.b2

    def backward(self, X, y_pred, y_true):
        # Backpropagation through the network
        # Calculate the gradient of the loss with respect to
        # the weights and biases - RMS' derivative by y_pred
        # E = (y - y0) ^ 2 / N
        # dE/dy = 2 * (y - y0)
        dE = self.rms_deriv(y_pred, y_true)

        # activation of output layer has no relu
        # dE/dW2 = dE/dy * dy/dW2
        # given y = W2.a1 + b2 => dy/dW2 = a1
        # so, dW2 = dE * a1
        dW2 = np.dot(self.a1.T, dE)
        db2 = np.sum(dE, axis=0, keepdims=True)

        # dE/dA1 = dE/dy * W2
        dA1 = np.dot(dE, self.W2.T)
        # dE/dZ1 = dE/dA1 * dA1/dZ1
        # so, dZ1 = dA1 * dr
        dZ1 = dA1 * self.relu_deriv(self.a1)

        # dE/dW1 = dE/dZ1 * dZ1/dW1
        # given Z1 = W1.X + b1 => dZ1/dW1 = X
        # so, dW1 = dZ1 * X
        dW1 = np.dot(X.T, dZ1)
        db1 = np.sum(dZ1, axis=0, keepdims=True)

        # Update the weights and biases using gradient descent
        self.W1 -= self.learning_rate * dW1
        self.b1 -= self.learning_rate * db1
        self.W2 -= self.learning_rate * dW2
        self.b2 -= self.learning_rate * db2

    def train(self, X_train, y_train, epochs):
        # Train the network using forward and backward propagation
        for epoch in range(epochs):
            # Forward pass: Calculate predicted y
            y_pred = self.forward(X_train)

            # Backward pass: Update weights
            self.backward(X_train, y_pred, y_train)

            if epoch % 100 == 0 or epoch == epochs - 1:
                print(f'Epoch {epoch}, Loss: {self.rms(y_pred, y_train):.4f}')

    def predict(self, X):
        # Make predictions on new data
        return self.forward(X)

    def rms(self, y_pred, y_true):
        # rms error
        return np.mean((y_pred - y_true) ** 2)

    def rms_deriv(self, y_pred, y_true):
        # rms error deriv
        return 2 * (y_pred - y_true) / len(y_pred)

    def relu(self, x):
        # ReLU activation function
        return np.maximum(0, x)

    def relu_deriv(self, x):
        # Derivative of the ReLU function
        return np.where(x > 0, 1, 0)


# Generate some synthetic data for training
X_train = np.random.rand(10000, 2)  # 10000 samples, 2 features
y_train = 2*X_train[:, 0] + X_train[:, 1]  # True function: 2*x1 + x2
y_train += np.random.rand(10000) / 10  # up to 10% noise in sample

# training data
X_test = np.array([[0.5, 0.2], [0.3, 0.7]])  # Test inputs
y_exp = 2*X_test[:, 0] + X_test[:, 1]

input_size = 2
output_size = 1

# Create and train the neural network
print("==== One layer ====")
nn = OneLayerNN(input_size, output_size, learning_rate=.1)
nn.train(X_train, y_train.reshape(-1, 1), epochs=1000)

# Test the trained network
y_pred = nn.predict(X_test)  # Predicted outputs
print('expected', y_exp, 'result', y_pred.flatten())

# Create and train the neural network
print("==== Two layer ====")
hidden_size = 3
nn = TwoLayerNN(input_size, hidden_size, output_size, learning_rate=.1)
nn.train(X_train, y_train.reshape(-1, 1), epochs=1000)

# Test the trained network
y_pred = nn.predict(X_test)  # Predicted outputs
print('expected', y_exp, 'result', y_pred.flatten())
