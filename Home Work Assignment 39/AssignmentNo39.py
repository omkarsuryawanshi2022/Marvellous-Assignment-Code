import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

# ==========================================
# 1. Dataset Loading
# ==========================================
print("--- 1. Dataset Loading ---")
# Reading the dataset from CSV
df = pd.read_csv('student_performance_ml.csv')
print("Dataset loaded successfully!")
print(df.head())
print()

# ==========================================
# 2. Data Analysis
# ==========================================
print("--- 2. Data Analysis ---")
print("Dataset Shape:", df.shape)
print("\nDataset Info:")
print(df.info())
print("\nMissing Values:")
print(df.isnull().sum())
print("\nSummary Statistics:")
print(df.describe())
print("\nClass Distribution (FinalResult):")
print(df['FinalResult'].value_counts())
print()

# ==========================================
# 3. Visualization
# ==========================================
print("--- 3. Visualization ---")
# Plotting distributions of key numerical features
fig, axes = plt.subplots(2, 3, figsize=(15, 9))
fig.suptitle('Feature Distributions & Relationships with Final Result', fontsize=14)

features = ['StudyHours', 'Attendance', 'PreviousScore', 'AssignmentsCompleted', 'SleepHours']

for idx, col in enumerate(features):
    row, col_idx = divmod(idx, 3)
    sns.boxplot(x='FinalResult', y=col, data=df, ax=axes[row, col_idx], palette='Set2')
    axes[row, col_idx].set_title(f'{col} vs Final Result')

# Target variable countplot in the last subplot
sns.countplot(x='FinalResult', data=df, ax=axes[1, 2], palette='pastel')
axes[1, 2].set_title('Target Class Distribution (Pass = 1, Fail = 0)')

plt.tight_layout()
plt.show()

# ==========================================
# 4. Train-Test Split
# ==========================================
print("--- 4. Train-Test Split ---")
# Features (X) and Target (y)
X = df[['StudyHours', 'Attendance', 'PreviousScore', 'AssignmentsCompleted', 'SleepHours']]
y = df['FinalResult']

# Splitting data (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"Training set size: {X_train.shape[0]} samples")
print(f"Testing set size:  {X_test.shape[0]} samples\n")

# ==========================================
# 5. Model Training & Task 1
# ==========================================
print("--- 5. Model Training ---")
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)
print("Decision Tree model trained successfully!\n")

# ==========================================
# 6. Predictions & Task 2
# ==========================================
print("--- 6. Predictions vs Actual Values ---")
y_pred = model.predict(X_test)

results_df = pd.DataFrame({
    'Actual_Result': y_test.values,
    'Predicted_Result': y_pred
})
print(results_df.head(10))
print()

# ==========================================
# Task 3: Calculate Accuracy in Percentage
# ==========================================
print("--- Task 3: Model Accuracy ---")
test_acc = accuracy_score(y_test, y_pred)
print(f"Model Accuracy on Test Set: {test_acc * 100:.2f}%\n")

# ==========================================
# Task 4: Confusion Matrix & Explanation
# ==========================================
print("--- Task 4: Confusion Matrix ---")
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Fail (0)', 'Pass (1)'])
disp.plot(cmap='Blues')
plt.title('Confusion Matrix')
plt.show()

tn, fp, fn, tp = cm.ravel()
print(f"True Positive (TP) : {tp}  -> Correctly predicted students who passed")
print(f"True Negative (TN) : {tn}  -> Correctly predicted students who failed")
print(f"False Positive (FP): {fp}  -> Incorrectly predicted as Pass when student actually failed (Type I Error)")
print(f"False Negative (FN): {fn}  -> Incorrectly predicted as Fail when student actually passed (Type II Error)\n")

# ==========================================
# Task 5: Overfitting / Underfitting Check
# ==========================================
print("--- Task 5: Compare Training vs Testing Accuracy ---")
train_acc = accuracy_score(y_train, model.predict(X_train))
print(f"Training Accuracy: {train_acc * 100:.2f}%")
print(f"Testing Accuracy:  {test_acc * 100:.2f}%")

if train_acc > test_acc + 0.10:
    print("Observation: The model shows signs of **Overfitting** because training accuracy is significantly higher than testing accuracy.")
elif train_acc < 0.70 and test_acc < 0.70:
    print("Observation: The model shows signs of **Underfitting** due to low overall performance.")
else:
    print("Observation: The model demonstrates **Good Fit** with generalized performance.")
print()

# ==========================================
# Task 6: Compare Different Tree Depths
# ==========================================
print("--- Task 6: Comparing Different Tree Depths ---")
depths = [1, 3, None]

for depth in depths:
    dt = DecisionTreeClassifier(max_depth=depth, random_state=42)
    dt.fit(X_train, y_train)
    tr_a = accuracy_score(y_train, dt.predict(X_train))
    te_a = accuracy_score(y_test, dt.predict(X_test))
    print(f"max_depth = {str(depth):<4} | Train Acc: {tr_a*100:6.2f}% | Test Acc: {te_a*100:6.2f}%")

print("\nObservations:")
print("- max_depth = 1: Causes Underfitting (High Bias) because a single split is too simple.")
print("- max_depth = 3: Balances complexity and generalization.")
print("- max_depth = None: Causes Overfitting (High Variance) as the tree memorizes training data.\n")

# ==========================================
# Task 7: Predict for a Specific Student
# ==========================================
print("--- Task 7: Predict for Specific Student ---")
sample_student = pd.DataFrame([{
    'StudyHours': 6,
    'Attendance': 85,
    'PreviousScore': 66,
    'AssignmentsCompleted': 7,
    'SleepHours': 7
}])

prediction = model.predict(sample_student)[0]
result_label = "Pass (1)" if prediction == 1 else "Fail (0)"

print("Student Details:")
print(sample_student.to_dict(orient='records')[0])
print(f"Predicted Final Result: {result_label}\n")

# ==========================================
# 8. Final Conclusion
# ==========================================
print("--- 8. Final Conclusion ---")
print("1. Decision Tree successfully predicts student academic performance based on behavioral metrics.")
print("2. Features like Attendance and StudyHours significantly influence the outcome.")
print("3. Unconstrained trees (max_depth=None) lead to overfitting, requiring hyperparameter tuning like setting `max_depth` to generalize well.")