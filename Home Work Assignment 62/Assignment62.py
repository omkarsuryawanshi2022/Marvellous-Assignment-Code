import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)


# ============================================================
# 1. Read data from CSV
# ============================================================

print("\n" + "=" * 60)
print("1. READ DATA FROM CSV")
print("=" * 60)

data = pd.read_csv("Employee_Attrition.csv")

print("\nComplete Dataset:")
print(data)


# ============================================================
# 2. Display first 5 records
# ============================================================

print("\n" + "=" * 60)
print("2. FIRST 5 RECORDS")
print("=" * 60)

print(data.head())


# ============================================================
# 3. Display column names
# ============================================================

print("\n" + "=" * 60)
print("3. COLUMN NAMES")
print("=" * 60)

print(data.columns)


# ============================================================
# 4. Display shape of dataset
# ============================================================

print("\n" + "=" * 60)
print("4. DATASET SHAPE")
print("=" * 60)

print("Rows    :", data.shape[0])
print("Columns :", data.shape[1])
print("Shape   :", data.shape)


# ============================================================
# 5. Display statistical summary
# ============================================================

print("\n" + "=" * 60)
print("5. STATISTICAL SUMMARY")
print("=" * 60)

print(data.describe())


# ============================================================
# 6. Check missing values
# ============================================================

print("\n" + "=" * 60)
print("6. CHECK MISSING VALUES")
print("=" * 60)

missing_values = data.isnull().sum()

print("\nMissing values in each column:")
print(missing_values)

if missing_values.sum() == 0:
    print("\nNo missing values found.")
else:
    print("\nMissing values are present.")


# ============================================================
# 7 & 8. Identify numerical and categorical features
# ============================================================

print("\n" + "=" * 60)
print("7 & 8. IDENTIFY NUMERICAL AND CATEGORICAL FEATURES")
print("=" * 60)


target_column = "Attrition"


feature_columns = [
    "Age",
    "MonthlyIncome",
    "YearsAtCompany",
    "TotalWorkingYears",
    "DistanceFromHome",
    "JobSatisfaction",
    "WorkLifeBalance",
    "OverTime",
    "NumCompaniesWorked",
    "TrainingTimesLastYear"
]


# Display original data types
print("\nData Types:")
print(data[feature_columns + [target_column]].dtypes)


# Numerical features
numerical_features = data[feature_columns].select_dtypes(
    include=["number"]
).columns.tolist()


# Categorical features
categorical_features = data[feature_columns].select_dtypes(
    include=["str", "category", "object"]
).columns.tolist()


print("\nNumerical Features:")

for feature in numerical_features:
    print("-", feature)


print("\nCategorical Features:")

for feature in categorical_features:
    print("-", feature)


print("\nTarget Variable:")
print("-", target_column)


# ============================================================
# 9. Convert OverTime into 0/1
# ============================================================

print("\n" + "=" * 60)
print("9. CONVERT OVERTIME INTO 0/1")
print("=" * 60)


print("\nBefore conversion:")
print(data["OverTime"].value_counts())


data["OverTime"] = data["OverTime"].map({
    "No": 0,
    "Yes": 1
})


print("\nAfter conversion:")
print(data["OverTime"].value_counts())


# ============================================================
# 10. Convert Attrition into 0/1
# ============================================================

print("\n" + "=" * 60)
print("10. CONVERT ATTRITION INTO 0/1")
print("=" * 60)


print("\nBefore conversion:")

# Note:
# At this point Attrition is still Yes/No
# because we have not converted it yet.

# If values are already numeric, this section will not be needed.
print(data["Attrition"].value_counts())


data["Attrition"] = data["Attrition"].map({
    "No": 0,
    "Yes": 1
})


print("\nAfter conversion:")
print(data["Attrition"].value_counts())


# ============================================================
# 11. Select input features X
# ============================================================

print("\n" + "=" * 60)
print("11. SELECT INPUT FEATURES X")
print("=" * 60)


X = data[
    [
        "Age",
        "MonthlyIncome",
        "YearsAtCompany",
        "TotalWorkingYears",
        "DistanceFromHome",
        "JobSatisfaction",
        "WorkLifeBalance",
        "OverTime",
        "NumCompaniesWorked",
        "TrainingTimesLastYear"
    ]
]


print("\nInput Features:")
print(X.head())

print("\nX Shape:")
print(X.shape)


# ============================================================
# 12. Select target variable Y
# ============================================================

print("\n" + "=" * 60)
print("12. SELECT TARGET VARIABLE Y")
print("=" * 60)


Y = data["Attrition"]


print("\nTarget:")
print(Y.head())

print("\nY Shape:")
print(Y.shape)


# ============================================================
# 13. Train Test Split
# ============================================================

print("\n" + "=" * 60)
print("13. TRAIN TEST SPLIT")
print("=" * 60)


X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.30,
    random_state=42,
    stratify=Y
)


print("\nTraining Input Shape :", X_train.shape)
print("Testing Input Shape  :", X_test.shape)

print("\nTraining Output Shape:", Y_train.shape)
print("Testing Output Shape :", Y_test.shape)


# ============================================================
# 14. Feature Scaling
# ============================================================

print("\n" + "=" * 60)
print("14. FEATURE SCALING")
print("=" * 60)


scaler = StandardScaler()


# Fit only on training data
X_train_scaled = scaler.fit_transform(X_train)


# Transform test data using same scaler
X_test_scaled = scaler.transform(X_test)


print("\nScaled Training Data:")
print(X_train_scaled[:5])


print("\nScaled Testing Data:")
print(X_test_scaled[:5])


# ============================================================
# 15. Create MLP / FNN Model
# ============================================================

print("\n" + "=" * 60)
print("15. CREATE MLP / FNN MODEL")
print("=" * 60)


model = MLPClassifier(
    hidden_layer_sizes=(8, 4),
    activation="relu",
    solver="adam",
    max_iter=1000,
    random_state=42
)


print("\nFNN Architecture:")
print("Input Layer       : 10 features")
print("Hidden Layer 1    : 8 neurons")
print("Hidden Layer 2    : 4 neurons")
print("Output Layer      : 1 output")
print("Activation        : ReLU")
print("Optimizer         : Adam")


print("\nModel:")
print(model)


# ============================================================
# 16. Train Model
# ============================================================

print("\n" + "=" * 60)
print("16. TRAIN MODEL")
print("=" * 60)


model.fit(
    X_train_scaled,
    Y_train
)


print("\nModel training completed successfully.")


# ============================================================
# 17. Display actual training iterations
# ============================================================

print("\n" + "=" * 60)
print("17. ACTUAL TRAINING ITERATIONS")
print("=" * 60)


print(
    "\nMaximum allowed iterations:",
    model.max_iter
)

print(
    "Actual iterations required:",
    model.n_iter_
)


# ============================================================
# 18. Calculate Training Accuracy
# ============================================================

print("\n" + "=" * 60)
print("18. TRAINING ACCURACY")
print("=" * 60)


Y_train_pred = model.predict(
    X_train_scaled
)


train_accuracy = accuracy_score(
    Y_train,
    Y_train_pred
)


print(
    "\nTraining Accuracy:",
    train_accuracy
)

print(
    "Training Accuracy (%):",
    train_accuracy * 100
)


# ============================================================
# 19. Calculate Testing Accuracy
# ============================================================

print("\n" + "=" * 60)
print("19. TESTING ACCURACY")
print("=" * 60)


Y_pred = model.predict(
    X_test_scaled
)


test_accuracy = accuracy_score(
    Y_test,
    Y_pred
)


print(
    "\nTesting Accuracy:",
    test_accuracy
)

print(
    "Testing Accuracy (%):",
    test_accuracy * 100
)


# ============================================================
# 20. Precision, Recall and F1 Score
# ============================================================

print("\n" + "=" * 60)
print("20. PRECISION, RECALL AND F1 SCORE")
print("=" * 60)


precision = precision_score(
    Y_test,
    Y_pred,
    pos_label=1,
    zero_division=0
)


recall = recall_score(
    Y_test,
    Y_pred,
    pos_label=1,
    zero_division=0
)


f1 = f1_score(
    Y_test,
    Y_pred,
    pos_label=1,
    zero_division=0
)


print("\nModel Performance:")

print("Accuracy  :", test_accuracy)
print("Precision :", precision)
print("Recall    :", recall)
print("F1 Score  :", f1)


# ============================================================
# 21. Confusion Matrix
# ============================================================

print("\n" + "=" * 60)
print("21. CONFUSION MATRIX")
print("=" * 60)


cm = confusion_matrix(
    Y_test,
    Y_pred,
    labels=[0, 1]
)


print("\nConfusion Matrix:")
print(cm)


print("\nMeaning:")
print("0 = Employee stays")
print("1 = Employee leaves")


# ============================================================
# Prediction Probability
# ============================================================

print("\n" + "=" * 60)
print("PREDICTION PROBABILITY")
print("=" * 60)


Y_probability = model.predict_proba(
    X_test_scaled
)


print("\nFirst 5 Prediction Probabilities:")
print(Y_probability[:5])


# ============================================================
# 22. Graphical Representation
# ============================================================

print("\n" + "=" * 60)
print("22. GRAPHICAL REPRESENTATION")
print("=" * 60)


# ------------------------------------------------------------
# Accuracy Graph
# ------------------------------------------------------------

plt.figure(figsize=(7, 5))


plt.bar(
    ["Training", "Testing"],
    [
        train_accuracy,
        test_accuracy
    ]
)


plt.ylim(0, 1)

plt.ylabel("Accuracy")

plt.title(
    "Employee Attrition MLP Model Accuracy"
)


plt.show()


# ------------------------------------------------------------
# Confusion Matrix Graph
# ------------------------------------------------------------

plt.figure(figsize=(6, 5))


plt.imshow(cm)


plt.title(
    "Employee Attrition Confusion Matrix"
)


plt.xlabel("Predicted")

plt.ylabel("Actual")


plt.xticks(
    [0, 1],
    ["Stay", "Leave"]
)


plt.yticks(
    [0, 1],
    ["Stay", "Leave"]
)


# Display values
for i in range(2):

    for j in range(2):

        plt.text(
            j,
            i,
            cm[i, j],
            ha="center",
            va="center"
        )


plt.show()


# ============================================================
# 23. Loss Curve
# ============================================================

print("\n" + "=" * 60)
print("23. LOSS CURVE")
print("=" * 60)


print(
    "\nNumber of loss values:",
    len(model.loss_curve_)
)


plt.figure(figsize=(7, 5))


plt.plot(
    model.loss_curve_
)


plt.xlabel(
    "Iterations"
)


plt.ylabel(
    "Loss"
)


plt.title(
    "MLP Training Loss Curve"
)


plt.show()


# ============================================================
# 24. Save and Load Model + Scaler
# ============================================================

print("\n" + "=" * 60)
print("24. SAVE AND LOAD MODEL")
print("=" * 60)


# ------------------------------------------------------------
# Save Model
# ------------------------------------------------------------

joblib.dump(
    model,
    "Employee_Attrition_fnn_model.pkl"
)


# ------------------------------------------------------------
# Save Scaler
# ------------------------------------------------------------

joblib.dump(
    scaler,
    "Employee_Attrition_scaler.pkl"
)


print(
    "\nModel and scaler saved successfully."
)


# ------------------------------------------------------------
# Load Model
# ------------------------------------------------------------

loaded_model = joblib.load(
    "Employee_Attrition_fnn_model.pkl"
)


# ------------------------------------------------------------
# Load Scaler
# ------------------------------------------------------------

loaded_scaler = joblib.load(
    "Employee_Attrition_scaler.pkl"
)


print(
    "Model and scaler loaded successfully."
)


# ============================================================
# 25. PredictAttrition() Function
# ============================================================

print("\n" + "=" * 60)
print("25. PREDICT ATTRITION FUNCTION")
print("=" * 60)


def PredictAttrition(employee_data):

    # Convert input data into DataFrame

    employee_df = pd.DataFrame(
        employee_data,
        columns=[
            "Age",
            "MonthlyIncome",
            "YearsAtCompany",
            "TotalWorkingYears",
            "DistanceFromHome",
            "JobSatisfaction",
            "WorkLifeBalance",
            "OverTime",
            "NumCompaniesWorked",
            "TrainingTimesLastYear"
        ]
    )


    # Scale using saved scaler

    employee_scaled = loaded_scaler.transform(
        employee_df
    )


    # Prediction

    prediction = loaded_model.predict(
        employee_scaled
    )


    # Probability

    probability = loaded_model.predict_proba(
        employee_scaled
    )


    # Convert numerical prediction
    # into meaningful result

    if prediction[0] == 1:

        result = "Employee will leave the company."

    else:

        result = "Employee will stay in the company."


    # Get probability of predicted class

    predicted_class_probability = (
        probability[0][prediction[0]] * 100
    )


    return result, predicted_class_probability


# ============================================================
# Test 5 Unseen Employees
# ============================================================

print("\n" + "-" * 60)
print("TESTING 5 UNSEEN EMPLOYEES")
print("-" * 60)


# Employee 1

employee_1 = [[
    35,
    75000,
    8,
    12,
    5,
    4,
    4,
    0,
    2,
    4
]]


# Employee 2

employee_2 = [[
    25,
    30000,
    1,
    3,
    20,
    2,
    2,
    1,
    4,
    2
]]


# Employee 3

employee_3 = [[
    42,
    90000,
    10,
    18,
    3,
    4,
    3,
    0,
    1,
    5
]]


# Employee 4

employee_4 = [[
    29,
    45000,
    2,
    5,
    15,
    2,
    2,
    1,
    3,
    3
]]


# Employee 5

employee_5 = [[
    50,
    110000,
    15,
    25,
    4,
    4,
    4,
    0,
    2,
    5
]]


# Store all employees

employees = [
    employee_1,
    employee_2,
    employee_3,
    employee_4,
    employee_5
]


# Test each employee

for i, employee in enumerate(
    employees,
    start=1
):

    result, probability = PredictAttrition(
        employee
    )


    print(
        f"\nEmployee {i}"
    )


    print(
        "Prediction:",
        result
    )


    print(
        "Prediction Probability:",
        round(probability, 2),
        "%"
    )


# ============================================================
# 26. Overfitting / Underfitting Analysis
# ============================================================

print("\n" + "=" * 60)
print("26. OVERFITTING / UNDERFITTING ANALYSIS")
print("=" * 60)


accuracy_difference = (
    train_accuracy - test_accuracy
)


print(
    "\nTraining Accuracy:",
    round(train_accuracy * 100, 2),
    "%"
)


print(
    "Testing Accuracy :",
    round(test_accuracy * 100, 2),
    "%"
)


print(
    "Accuracy Difference:",
    round(accuracy_difference * 100, 2),
    "percentage points"
)


# ------------------------------------------------------------
# Basic interpretation
# ------------------------------------------------------------

if (
    train_accuracy < 0.75
    and test_accuracy < 0.75
):

    print(
        "\nAnalysis: The model may be underfitting."
    )

    print(
        "Both training and testing accuracy are relatively low."
    )


elif (
    accuracy_difference > 0.10
):

    print(
        "\nAnalysis: The model may be overfitting."
    )

    print(
        "Training accuracy is considerably higher than testing accuracy."
    )


else:

    print(
        "\nAnalysis: The model appears to generalize reasonably well."
    )

    print(
        "Training and testing accuracy are relatively close."
    )


# ============================================================
# Final Summary
# ============================================================

print("\n" + "=" * 60)
print("FINAL MODEL SUMMARY")
print("=" * 60)


print(
    "\nArchitecture:"
)

print(
    "Input Layer → 8 Neurons → 4 Neurons → Output Layer"
)


print(
    "\nActual Training Iterations:",
    model.n_iter_
)


print(
    "Training Accuracy:",
    round(train_accuracy * 100, 2),
    "%"
)


print(
    "Testing Accuracy:",
    round(test_accuracy * 100, 2),
    "%"
)


print(
    "Precision:",
    round(precision, 4)
)


print(
    "Recall:",
    round(recall, 4)
)


print(
    "F1 Score:",
    round(f1, 4)
)


print(
    "\nEmployee Attrition FNN project completed successfully."
)