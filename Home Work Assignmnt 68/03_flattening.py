# Flattening in CNN

matrix = [
    [6, 4],
    [8, 6]
]

# Convert 2D matrix to 1D vector
flatten_output = []

for row in matrix:
    for value in row:
        flatten_output.append(value)

print("Input Matrix:")
for row in matrix:
    print(row)

print("\nFlattened Output:")
print(flatten_output)

# Pass flattened vector to a simple fully connected layer
weights = [0.1, 0.2, 0.3, 0.4]
bias = 1.0

output = 0

for value, weight in zip(flatten_output, weights):
    output += value * weight

output += bias

print("\nFully Connected Layer Output:")
print(output)

print("\nRole of Flattening:")
print("Flattening converts a 2D feature map into a 1D vector")
print("so it can be passed to a fully connected (Dense) layer.")
