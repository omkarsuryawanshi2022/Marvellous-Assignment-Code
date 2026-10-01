import math

# Input values
x1 = 2
x2 = 3

# Weights
w1 = 0.4
w2 = 0.6

# Bias
bias = 0.5

# 1. Calculate weighted sum
weighted_sum = (x1 * w1) +(x2 *  w2) +bias

print("Weighed sum:",weighted_sum)

# 2. Apply sigmoid activation function

sigmoid_output = 1 / (1 + math.exp(-weighted_sum))

# 3. Display final output
print("Sigmoid Output:", sigmoid_output)

# 4. Explain output

if 0 <= sigmoid_output < 0.5:
       print("The output is between 0 and 1.")
else:
        print("The output is outside the range 0 to 1.")
