import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score

# ==========================================
# 0. Load Dataset & Baseline Model Setup
# ==========================================
df = pd.read_csv('student_performance_ml.csv')

X = df[['StudyHours', 'Attendance', 'PreviousScore', 'AssignmentsCompleted', 'SleepHours']]
y = df['FinalResult']

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train baseline Decision Tree
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
baseline_acc = accuracy_score(y_test, y_pred)
print(f"Baseline Accuracy: {baseline_acc * 100:.2f}%\n")


# ==========================================
# Task 1: Feature Importances
# ==========================================
print("--- Task 1: Feature Importances ---")
importances = pd.Series(model.feature_importances_, index=X.columns)
print("Feature Importance Scores:")
print(importances.sort_values(ascending=False))

most_important = importances.idxmax()
least_important = importances.idxmin()
print(f"\nMost Important Feature: {most_important}")
print(f"Least Important Feature: {least_important}\n")


# ==========================================
# Task 2: Remove 'SleepHours' Column
# ==========================================
print("--- Task 2: Remove 'SleepHours' Column ---")
X_no_sleep = X.drop(columns=['SleepHours'])

X_tr2, X_te2, y_tr2, y_te2 = train_test_split(
    X_no_sleep, y, test_size=0.2, random_state=42
)

model2 = DecisionTreeClassifier(random_state=42)
model2.fit(X_tr2, y_tr2)
acc_task2 = accuracy_score(y_te2, model2.predict(X_te2))

print(f"Baseline Accuracy: {baseline_acc * 100:.2f}%")
print(f"Accuracy without SleepHours: {acc_task2 * 100:.2f}%")
if acc_task2 >= baseline_acc:
    print("Impact: Removing 'SleepHours' had minimal or positive effect because it had low feature importance.")
else:
    print("Impact: Performance dropped slightly due to loss of variance captured by 'SleepHours'.")
print()


# ==========================================
# Task 3: Train using only 'StudyHours' and 'Attendance'
# ==========================================
print("--- Task 3: Train using StudyHours & Attendance only ---")
X_sub = X[['StudyHours', 'Attendance']]

X_tr3, X_te3, y_tr3, y_te3 = train_test_split(
    X_sub, y, test_size=0.2, random_state=42
)

model3 = DecisionTreeClassifier(random_state=42)
model3.fit(X_tr3, y_tr3)
acc_task3 = accuracy_score(y_te3, model3.predict(X_te3))

print(f"Baseline Accuracy (Full Features): {baseline_acc * 100:.2f}%")
print(f"Accuracy (StudyHours + Attendance): {acc_task3 * 100:.2f}%\n")


# ==========================================
# Task 4: Predict Results for 5 New Students
# ==========================================
print("--- Task 4: Predict for 5 New Students ---")
new_students = pd.DataFrame({
    'StudyHours': [8, 2, 6, 1, 5],
    'Attendance': [95, 50, 80, 40, 75],
    'PreviousScore': [88, 45, 70, 35, 65],
    'AssignmentsCompleted': [10, 2, 7, 1, 6],
    'SleepHours': [7, 6, 8, 5, 7]
})

new_preds = model.predict(new_students)
new_students['Predicted_FinalResult'] = ['Pass' if p == 1 else 'Fail' for p in new_preds]
print(new_students)
print()


# ==========================================
# Task 5: Calculate Accuracy Manually
# ==========================================
print("--- Task 5: Manual Accuracy Calculation ---")
correct_predictions = (y_test.values == y_pred).sum()
total_predictions = len(y_test)
manual_accuracy = correct_predictions / total_predictions

print(f"Manual Accuracy: {manual_accuracy:.4f}")
print(f"Sklearn Accuracy: {baseline_acc:.4f}")
print(f"Matches sklearn? {manual_accuracy == baseline_acc}\n")


# ==========================================
# Task 6: Identify Misclassified Students
# ==========================================
print("--- Task 6: Misclassified Students Analysis ---")
misclassified_mask = (y_test.values != y_pred)
misclassified_df = X_test[misclassified_mask].copy()
misclassified_df['Actual'] = y_test[misclassified_mask]
misclassified_df['Predicted'] = y_pred[misclassified_mask]

print(f"Total Misclassified Students: {len(misclassified_df)}")
print("\nMisclassified Rows:")
print(misclassified_df)
print()


# ==========================================
# Task 7: Effect of 'random_state'
# ==========================================
print("--- Task 7: Experimenting with random_state ---")
for rs in [0, 10, 42]:
    X_tr_rs, X_te_rs, y_tr_rs, y_te_rs = train_test_split(
        X, y, test_size=0.2, random_state=rs
    )
    m = DecisionTreeClassifier(random_state=rs)
    m.fit(X_tr_rs, y_tr_rs)
    acc = accuracy_score(y_te_rs, m.predict(X_te_rs))
    print(f"random_state = {rs} -> Testing Accuracy: {acc * 100:.2f}%")
print("Explanation: Accuracy varies because random_state alters how data is split into train and test sets.\n")


# ==========================================
# Task 8: Decision Tree Visualization
# ==========================================
print("--- Task 8: Decision Tree Visualization ---")
plt.figure(figsize=(12, 8))
plot_tree(
    model, 
    feature_names=X.columns, 
    class_names=['Fail', 'Pass'], 
    filled=True
)
plt.title("Decision Tree Visualization")
plt.show()

print("Root Node Feature Analysis:")
print(f"- Feature at Root Node: {X.columns[model.tree_.feature[0]]}")
print("- Reason: This feature yields the highest Information Gain (or maximum Gini Impurity reduction) across the dataset.\n")


# ==========================================
# Task 9: Feature Engineering (PerformanceIndex)
# ==========================================
print("--- Task 9: Feature Engineering ---")
X_fe = X.copy()
X_fe['PerformanceIndex'] = (X_fe['StudyHours'] * 2) + X_fe['Attendance']

X_tr9, X_te9, y_tr9, y_te9 = train_test_split(
    X_fe, y, test_size=0.2, random_state=42
)

model9 = DecisionTreeClassifier(random_state=42)
model9.fit(X_tr9, y_tr9)
acc_task9 = accuracy_score(y_te9, model9.predict(X_te9))

print(f"Accuracy before feature engineering: {baseline_acc * 100:.2f}%")
print(f"Accuracy after adding PerformanceIndex: {acc_task9 * 100:.2f}%\n")


# ==========================================
# Task 10: Overfitting Analysis (max_depth=None)
# ==========================================
print("--- Task 10: Overfitting Analysis ---")
model10 = DecisionTreeClassifier(max_depth=None, random_state=42)
model10.fit(X_train, y_train)

train_acc = accuracy_score(y_train, model10.predict(X_train))
test_acc = accuracy_score(y_test, model10.predict(X_test))

print(f"Training Accuracy: {train_acc * 100:.2f}%")
print(f"Testing Accuracy:  {test_acc * 100:.2f}%")

print("\nWhy this happens (Overfitting):")
print("- When max_depth=None, the tree grows fully until every leaf is pure, perfectly memorizing the noise in the training data (100% training accuracy).")
print("- Consequently, it struggles to generalize to unseen testing data, leading to a noticeable drop in test accuracy.")