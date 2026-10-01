# ============================================================
# Customer Churn Prediction using Artificial Neural Network
# ============================================================

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report


# ============================================================
# STEP 1: CREATE / LOAD DATASET
# ============================================================

# Features:
# [Age, Monthly Charges, Tenure, Complaints, Support Calls]

X = np.array([
    [25,  500, 12, 1,  2],
    [30,  700, 24, 0,  1],
    [45, 1200,  6, 5,  8],
    [50, 1500,  5, 6, 10],
    [28,  600, 18, 1,  1],
    [35,  800, 30, 0,  0],
    [48, 1400,  4, 7,  9],
    [52, 1600,  3, 8, 12],
    [27,  550, 20, 0,  1],
    [42, 1300,  8, 4,  7]
])

# Target:
# 0 = Customer will stay
# 1 = Customer will leave

y = np.array([
    0,
    0,
    1,
    1,
    0,
    0,
    1,
    1,
    0,
    1
])


# Create DataFrame
columns = [
    "Age",
    "Monthly Charges",
    "Tenure",
    "Complaints",
    "Support Calls"
]

df = pd.DataFrame(X, columns=columns)
df["Target"] = y

print("========== DATASET ==========")
print(df)


# ============================================================
# STEP 2: CLEAN DATA
# ============================================================

print("\n========== DATA CLEANING ==========")

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Check duplicate rows
print("\nDuplicate rows:", df.duplicated().sum())

# Remove duplicate rows if any
df = df.drop_duplicates()

print("\nCleaned dataset:")
print(df)


# Separate features and target
X = df[columns]
y = df["Target"]


# ============================================================
# STEP 3: TRAIN / TEST SPLIT + STANDARD SCALER
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\n========== DATA SPLIT ==========")

print("Training samples:", len(X_train))
print("Testing samples :", len(X_test))


# Create StandardScaler
scaler = StandardScaler()

# Fit scaler only on training data
X_train_scaled = scaler.fit_transform(X_train)

# Transform test data
X_test_scaled = scaler.transform(X_test)

print("\n========== STANDARD SCALER ==========")

print("Scaled training data:")
print(X_train_scaled)


# ============================================================
# STEP 4: TRAIN FNN / ANN MODEL
# ============================================================

print("\n========== TRAINING FNN MODEL ==========")

# Feedforward Neural Network
model = MLPClassifier(
    hidden_layer_sizes=(10, 5),
    activation="relu",
    solver="adam",
    learning_rate_init=0.01,
    max_iter=2000,
    random_state=42
)

# Train model
model.fit(X_train_scaled, y_train)

print("FNN model training completed.")


# ============================================================
# STEP 5: EVALUATE MODEL
# ============================================================

print("\n========== MODEL EVALUATION ==========")

# Predict test data
y_pred = model.predict(X_test_scaled)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Actual values   :", y_test.to_numpy())
print("Predicted values:", y_pred)

print("\nAccuracy:", accuracy)
print("Accuracy percentage:", accuracy * 100, "%")

# Classification report
print("\n========== CLASSIFICATION REPORT ==========")

print(
    classification_report(
        y_test,
        y_pred,
        target_names=[
            "Customer will stay",
            "Customer will leave"
        ],
        zero_division=0
    )
)


# ============================================================
# STEP 6: PREDICT NEW CUSTOMER
# ============================================================

print("\n========== NEW CUSTOMER PREDICTION ==========")

# New customer from the question
# [Age, Monthly Charges, Tenure, Complaints, Support Calls]

new_customer = np.array([
    [46, 1450, 5, 6, 9]
])

print("New customer:")
print(new_customer)


# IMPORTANT:
# Use the SAME scaler that was fitted on training data
new_customer_scaled = scaler.transform(new_customer)


# Predict class
prediction = model.predict(new_customer_scaled)[0]

# Predict probability
probability = model.predict_proba(new_customer_scaled)[0][1]


print("\nChurn probability:", probability)
print("Prediction:", prediction)


# Convert prediction into meaningful output
if prediction == 0:
    print("Result: Customer will stay")
else:
    print("Result: Customer will leave")