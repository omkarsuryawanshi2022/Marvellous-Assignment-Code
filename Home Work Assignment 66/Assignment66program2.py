import numpy as np
import matplotlib.pyplot as plt

# Activation functions

def relu(x):
    return np.maximum(0, x)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def tanh(x):
    return np.tanh(x)


# 1. Accept input values from -10 to 10
x = np.linspace(-10, 10, 400)

# Calculate activation function outputs
relu_output = relu(x)
sigmoid_output = sigmoid(x)
tanh_output = tanh(x)


# 2. Plot all activation functions
plt.figure(figsize=(10, 6))

plt.plot(x, relu_output, label="ReLU")
plt.plot(x, sigmoid_output, label="Sigmoid")
plt.plot(x, tanh_output, label="Tanh")

plt.title("Activation Functions")
plt.xlabel("Input Value")
plt.ylabel("Output")
plt.axhline(0, linewidth=0.8)
plt.axvline(0, linewidth=0.8)
plt.grid(True)
plt.legend()

plt.show()