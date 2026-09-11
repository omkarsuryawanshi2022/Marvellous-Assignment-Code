import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler

# ============================================================
# 1. READ & UNDERSTAND DATASET
# ============================================================
print("\n" + "=" * 60)
print("1. LOAD AND UNDERSTAND DATASET")
print("=" * 60)

data = pd.read_csv("Loan_Default.csv")
print("\nFirst 5 Records:")
print(data.head())

print("\nDataset Shape:", data.shape)
print("\nStatistical Summary:")
print(data.describe())

# ============================================================
# 2. EXPLORATORY DATA ANALYSIS (EDA)
# ============================================================
print("\n" + "=" * 60)
print("2. EXPLORATORY DATA ANALYSIS")
print("=" * 60)

# Plot numerical distribution summary
data.hist(figsize=(10, 8), bins=15)
plt.tight_layout()
plt.suptitle("Feature Distributions", y=1.02)
plt.show()

# ============================================================
# 3. MISSING VALUES CHECK
# ============================================================
print("\n" + "=" * 60)
print("3. MISSING VALUES CHECK")
print("=" * 60)

missing_values = data.isnull().sum()
print(missing_values)

# ============================================================
# 4. TARGET CLASS BALANCE CHECK
# ============================================================
print("\n" + "=" * 60)
print("4. CHECK TARGET CLASS BALANCE")
print("=" * 60)

target_counts = data["Default"].value_counts()
target_percentages = data["Default"].value_counts(normalize=True) * 100

print("Counts:\n", target_counts)
print("\nPercentage:\n", target_percentages)

# ============================================================
# COMPLETED TASK 5: Encode categorical variables
# ============================================================
print("\n" + "=" * 60)
print("5. ENCODE CATEGORICAL VARIABLES")
print("=" * 60)

# Convert PreviousDefault strings directly to integers
data["PreviousDefault"] = (
    data["PreviousDefault"].astype(str).str.strip().map({"No": 0, "Yes": 1})
)

# One-Hot Encode HomeOwnership (Rent/Own/Mortgage)
data = pd.get_dummies(data, columns=["HomeOwnership"], drop_first=True)

# Convert Target variable if string
if data["Default"].dtype == "O":
    data["Default"] = (
        data["Default"].astype(str).str.strip().map({"No": 0, "Yes": 1})
    )

print("Columns after encoding:")
print(data.columns.tolist())

# ============================================================
# 6. SEPARATE X AND Y
# ============================================================
print("\n" + "=" * 60)
print("6. SEPARATE X AND Y")
print("=" * 60)

X = data.drop("Default", axis=1)
Y = data["Default"]

print("X shape:", X.shape)
print("Y shape:", Y.shape)

# ============================================================
# 7 & 8. TRAIN TEST SPLIT & STRATIFICATION EXPLANATION
# ============================================================
print("\n" + "=" * 60)
print("7 & 8. TRAIN-TEST SPLIT & STRATIFICATION EXPLANATION")
print("=" * 60)

print("Explanation: Stratified splitting ensures that the proportion of positive")
print("and negative loan defaults in both training and testing datasets remains equal")
print("to the original dataset distribution, preventing bias during model evaluation.")

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.30, random_state=42, stratify=Y
)

# ============================================================
# 9. FEATURE SCALING
# ============================================================
print("\n" + "=" * 60)
print("9. FEATURE SCALING")
print("=" * 60)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ============================================================
# 10 & 11. CREATE AND TRAIN BASELINE MLP
# ============================================================
print("\n" + "=" * 60)
print("10 & 11. BASELINE MLP CLASSIFIER TRAINING")
print("=" * 60)

model = MLPClassifier(
    hidden_layer_sizes=(32, 16),
    activation="relu",
    solver="adam",
    max_iter=1000,
    random_state=42,
)

model.fit(X_train_scaled, Y_train)

# ============================================================
# 12 - 15. EVALUATION METRICS
# ============================================================
print("\n" + "=" * 60)
print("12 - 15. MODEL EVALUATION")
print("=" * 60)

Y_pred = model.predict(X_test_scaled)

print("Accuracy        :", accuracy_score(Y_test, Y_pred))
print("Precision       :", precision_score(Y_test, Y_pred, zero_division=0))
print("Recall          :", recall_score(Y_test, Y_pred, zero_division=0))
print("F1 Score        :", f1_score(Y_test, Y_pred, zero_division=0))

cm = confusion_matrix(Y_test, Y_pred, labels=[0, 1])
print("\nConfusion Matrix:\n", cm)

print("\nClassification Report:\n")
print(classification_report(Y_test, Y_pred))

# ============================================================
# 16. PLOT TRAINING LOSS
# ============================================================
print("\n" + "=" * 60)
print("16. PLOT TRAINING LOSS")
print("=" * 60)

plt.figure(figsize=(7, 4))
plt.plot(model.loss_curve_)
plt.xlabel("Iterations")
plt.ylabel("Loss")
plt.title("MLP Training Loss Curve")
plt.show()

# Save Scaler and Model for Inference
joblib.dump(model, "Loan_Default_MLP.pkl")
joblib.dump(scaler, "Loan_Default_Scaler.pkl")

# ============================================================
# 17. TEST MODEL ON NEW LOAN APPLICANTS
# ============================================================
print("\n" + "=" * 60)
print("17. TEST MODEL ON NEW APPLICANTS")
print("=" * 60)


def PredictLoanDefault(applicant_df):
    scaled_df = scaler.transform(applicant_df)
    pred = model.predict(scaled_df)[0]
    prob = model.predict_proba(scaled_df)[0][pred] * 100

    status = (
        "High Default Risk (1)" if pred == 1 else "Low Default Risk (0)"
    )
    return status, round(prob, 2)


# Sample applicant matching post-encoded columns
sample_applicant = X_test.iloc[0:1]
status, probability = PredictLoanDefault(sample_applicant)
print(f"Prediction: {status} | Confidence: {probability}%")

# ============================================================
# HYPERPARAMETER EXPERIMENTS
# ============================================================
print("\n" + "=" * 60)
print("HYPERPARAMETER EXPERIMENTS")
print("=" * 60)

# Experiment 1 — Activation Functions
print("\n--- Experiment 1: Activation Functions ---")
activations = ["identity", "logistic", "tanh", "relu"]
for act in activations:
    exp_model = MLPClassifier(
        hidden_layer_sizes=(32, 16),
        activation=act,
        solver="adam",
        max_iter=1000,
        random_state=42,
    )
    exp_model.fit(X_train_scaled, Y_train)
    acc = accuracy_score(Y_test, exp_model.predict(X_test_scaled))
    print(f"Activation: {act:<10} | Accuracy: {acc:.4f}")

# Experiment 2 — Hidden Layers
print("\n--- Experiment 2: Hidden Layers ---")
architectures = [(10,), (20, 10), (50, 25), (100, 50, 25)]
for arch in architectures:
    exp_model = MLPClassifier(
        hidden_layer_sizes=arch,
        activation="relu",
        solver="adam",
        max_iter=1000,
        random_state=42,
    )
    exp_model.fit(X_train_scaled, Y_train)
    acc = accuracy_score(Y_test, exp_model.predict(X_test_scaled))
    print(f"Layers: {str(arch):<15} | Accuracy: {acc:.4f}")

# Experiment 3 — Learning Rates
print("\n--- Experiment 3: Learning Rate ---")
rates = [0.0001, 0.001, 0.01, 0.1]
for lr in rates:
    exp_model = MLPClassifier(
        hidden_layer_sizes=(32, 16),
        activation="relu",
        solver="adam",
        learning_rate_init=lr,
        max_iter=1000,
        random_state=42,
    )
    exp_model.fit(X_train_scaled, Y_train)
    acc = accuracy_score(Y_test, exp_model.predict(X_test_scaled))
    print(f"Learning Rate: {lr:<8} | Accuracy: {acc:.4f}")