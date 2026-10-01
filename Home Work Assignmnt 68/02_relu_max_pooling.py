# ReLU and 2x2 Max Pooling

feature_map = [
    [3, 3, 3],
    [0, 0, 0],
    [-3, -3, -3]
]

# ReLU
relu_output = []

for row in feature_map:
    relu_row = []

    for value in row:
        if value < 0:
            relu_row.append(0)
        else:
            relu_row.append(value)

    relu_output.append(relu_row)

print("Input Feature Map:")
for row in feature_map:
    print(row)

print("\nReLU Output:")
for row in relu_output:
    print(row)


# 2x2 Max Pooling
pooled_output = []

for i in range(len(relu_output) - 1):
    pooled_row = []

    for j in range(len(relu_output[0]) - 1):
        region = [
            relu_output[i][j:j+2],
            relu_output[i+1][j:j+2]
        ]

        maximum = max(
            region[0][0],
            region[0][1],
            region[1][0],
            region[1][1]
        )

        print("\nPooling Region:")
        for row in region:
            print(row)

        print("Maximum =", maximum)
        pooled_row.append(maximum)

    pooled_output.append(pooled_row)

print("\nMax Pooling Output:")
for row in pooled_output:
    print(row)

print("\nPooling reduces the spatial size of the feature map.")
