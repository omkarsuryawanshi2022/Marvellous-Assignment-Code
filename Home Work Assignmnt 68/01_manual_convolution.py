# Manual Convolution

image = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

kernel = [
    [-1, -1, -1],
    [0, 0, 0],
    [1, 1, 1]
]

feature_map = []

for i in range(len(image) - 2):
    output_row = []

    for j in range(len(image[0]) - 2):
        region = [image[i+r][j:j+3] for r in range(3)]

        print("\nRegion:")
        for row in region:
            print(row)

        total = 0
        print("Calculation:")

        for r in range(3):
            for c in range(3):
                total += region[r][c] * kernel[r][c]

        print("Output =", total)
        output_row.append(total)

    feature_map.append(output_row)

print("\nFeature Map:")
for row in feature_map:
    print(row)
