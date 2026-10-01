# Artificial Neural Network - Weight Update

# 1. Input, weight, bias, target output and learning rate
x = 2.0
weight = 0.5
bias = 0.1
target = 1.0
learning_rate = 0.1

# 2. Calculate prediction
prediction = (x * weight) + bias

# 3. Calculate error
error = target - prediction

# 4. Calculate gradient and update weight
gradient = -2 * x * error

old_weight = weight

weight = weight - (learning_rate * gradient)

# Update bias as well
bias = bias - (learning_rate * (-2 * error))

# 5. Display results
print("Input:", x)
print("Target Output:", target)
print("Learning Rate:", learning_rate)

print("\nPrediction:", prediction)
print("Error:", error)

print("\nOld Weight:", old_weight)
print("Updated Weight:", weight)

print("Updated Bias:", bias)