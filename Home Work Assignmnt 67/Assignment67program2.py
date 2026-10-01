# ============================================================
# LOAN APPROVAL PREDICTION USING FNN / ANN
# ============================================================

import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report


# ============================================================
# STEP 1: CREATE DATASET
# ============================================================

# Features:
# [Income, Credit Score, Loan Amount, Existing EMI, Employment Status]

X = np.array([
    [25000, 600, 200000, 10000, 0],
    [40000, 700, 300000,  8000, 1],
    [60000, 750, 500000, 12000, 1],
    [20000, 550, 150000, 15000, 0],
    [80000, 700, 700000, 10000, 1],
    [35000, 650, 250000,  9000, 1],
    [18000, 500, 100000, 12000, 0],
    [90000, 850, 800000, 15000, 1],
    [30000, 580, 200000, 14000, 0],
    [70000, 780, 600000, 10000, 1]
])


# Target values
# 0 = Loan Rejected
# 1 = Loan Approved

y = np.array([
    0,
    1,
    1,
    0,
    1,
    1,
    0,
    1,
    0,
    1
])


print("======================================")
print("       LOAN APPROVAL DATASET")
print("======================================")

print("\nFeatures:")
print("[Income, Credit Score, Loan Amount, Existing EMI, Employment Status]")

print("\nX =")
print(X)

print("\ny =")
print(y)


# ============================================================
# STEP 1: PREPROCESS CATEGORICAL VALUES
# ============================================================

print("\n======================================")
print("STEP 1: PREPROCESS CATEGORICAL VALUES")
print("======================================")

# Employment Status is already encoded:
#
# 0 = Not Stable
# 1 = Stable
#
# Therefore, no additional encoding is required.

print("\nEmployment Status is already encoded.")
print("0 = Not Stable")
print("1 = Stable")


# ============================================================
# STEP 2: SPLIT DATA AND APPLY SCALING
# ============================================================

print("\n======================================")
print("STEP 2: APPLY SCALING")
print("======================================")

# Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining samples:", len(X_train))
print("Testing samples :", len(X_test))


# Create StandardScaler
scaler = StandardScaler()

# Fit scaler on training data
X_train_scaled = scaler.fit_transform(X_train)

# Transform test data
X_test_scaled = scaler.transform(X_test)

print("\nScaled Training Data:")
print(X_train_scaled)


# ============================================================
# STEP 3: TRAIN FNN MODEL
# ============================================================

print("\n======================================")
print("STEP 3: TRAIN FNN MODEL")
print("======================================")


# Feedforward Neural Network
model = MLPClassifier(
    hidden_layer_sizes=(10, 5),
    activation="relu",
    solver="adam",
    learning_rate_init=0.01,
    max_iter=5000,
    random_state=42
)


# Train the model
model.fit(X_train_scaled, y_train)

print("\nFNN Model Training Completed!")


# ============================================================
# STEP 4: EVALUATE MODEL
# ============================================================

print("\n======================================")
print("STEP 4: EVALUATE MODEL")
print("======================================")


# Make predictions on test data
y_pred = model.predict(X_test_scaled)


# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)


print("\nActual Values:")
print(y_test)

print("\nPredicted Values:")
print(y_pred)

print("\nAccuracy:", accuracy)

print("Accuracy Percentage:", accuracy * 100, "%")


# Classification report
print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred,
        target_names=[
            "Loan Rejected",
            "Loan Approved"
        ],
        zero_division=0
    )
)


# ============================================================
# STEP 5: PREDICT NEW APPLICANT
# ============================================================

print("\n======================================")
print("STEP 5: NEW APPLICANT PREDICTION")
print("======================================")


# New applicant from the question
#
# [Income, Credit Score, Loan Amount, Existing EMI,
#  Employment Status]

new_applicant = np.array([
    [55000, 720, 400000, 10000, 1]
])


print("\nNew Applicant:")
print(new_applicant)


# IMPORTANT:
# Use the SAME scaler that was fitted on training data

new_applicant_scaled = scaler.transform(new_applicant)


# Predict class
prediction = model.predict(new_applicant_scaled)[0]


# Predict probability
probability = model.predict_proba(
    new_applicant_scaled
)[0][1]


print("\nApproval Probability:", probability)

print("Prediction:", prediction)


# Convert prediction into meaningful result

if prediction == 1:
    print("\nResult: Loan Approved")
else:
    print("\nResult: Loan Rejected")