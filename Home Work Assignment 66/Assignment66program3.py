import math

# Actual values
actual = [1, 0, 1, 1, 0]

# Predicted values
# For BCE, predictions should be probabilities between 0 and 1
predicted = [0.9, 0.2, 0.8, 0.7, 0.1]


# 1. Calculate Mean Squared Error (MSE)
def mean_squared_error(actual, predicted):
    total = 0

    for a, p in zip(actual, predicted):
        total += (a - p) ** 2

    mse = total / len(actual)

    return mse


# 2. Calculate Binary Cross-Entropy
def binary_cross_entropy(actual, predicted):
    total = 0

    for a, p in zip(actual, predicted):
        total += -(a * math.log(p) + (1 - a) * math.log(1 - p))

    bce = total / len(actual)

    return bce


# Calculate losses
mse_loss = mean_squared_error(actual, predicted)
bce_loss = binary_cross_entropy(actual, predicted)


# 3 & 4. Display calculated losses
print("Actual Values:   ", actual)
print("Predicted Values:", predicted)

print("\nMean Squared Error (MSE):", mse_loss)
print("Binary Cross-Entropy (BCE):", bce_loss)