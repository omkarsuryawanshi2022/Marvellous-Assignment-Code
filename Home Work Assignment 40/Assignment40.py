import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set visual theme
sns.set_theme(style="whitegrid")

# ==========================================
# 1. Load File & Display Basic Info
# ==========================================
print("=== QUESTION 1 ===")
df = pd.read_csv('student_performance_ml.csv')

print("\n--- First 5 Records ---")
print(df.head())

print("\n--- Last 5 Records ---")
print(df.tail())

print(f"\nTotal Rows and Columns: {df.shape[0]} rows, {df.shape[1]} columns")

print("\n--- List of Column Names ---")
print(df.columns.tolist())

print("\n--- Data Types ---")
print(df.dtypes)


# ==========================================
# 2. Count Students by Outcome
# ==========================================
print("\n=== QUESTION 2 ===")
total_students = len(df)
passed_students = (df['FinalResult'] == 1).sum()
failed_students = (df['FinalResult'] == 0).sum()

print(f"Total Students: {total_students}")
print(f"Passed Students (FinalResult = 1): {passed_students}")
print(f"Failed Students (FinalResult = 0): {failed_students}")


# ==========================================
# 3. Calculate Key Statistics
# ==========================================
print("\n=== QUESTION 3 ===")
print(f"Average StudyHours: {df['StudyHours'].mean():.2f} hrs")
print(f"Average Attendance: {df['Attendance'].mean():.2f}%")
print(f"Maximum PreviousScore: {df['PreviousScore'].max()}")
print(f"Minimum SleepHours: {df['SleepHours'].min()} hrs")


# ==========================================
# 4. Distribution & Dataset Balance Analysis
# ==========================================
print("\n=== QUESTION 4 ===")
counts = df['FinalResult'].value_counts()
percentages = df['FinalResult'].value_counts(normalize=True) * 100

print("Counts:\n", counts)
print("\nPercentages (%):\n", percentages.round(2))

# ==========================================
# 5. Analysis: Impact of StudyHours & Attendance
# ==========================================
print("\n=== QUESTION 5 ===")
mean_study_pass = df[df['FinalResult'] == 1]['StudyHours'].mean()
mean_study_fail = df[df['FinalResult'] == 0]['StudyHours'].mean()

mean_att_pass = df[df['FinalResult'] == 1]['Attendance'].mean()
mean_att_fail = df[df['FinalResult'] == 0]['Attendance'].mean()

print(f"Average Study Hours -> Passed: {mean_study_pass:.2f} hrs | Failed: {mean_study_fail:.2f} hrs")
print(f"Average Attendance  -> Passed: {mean_att_pass:.2f}% | Failed: {mean_att_fail:.2f}%")


# ==========================================
# 6. Histogram of StudyHours
# ==========================================
plt.figure(figsize=(8, 5))
sns.histplot(df['StudyHours'], kde=True, color='skyblue', bins=10)
plt.title('Histogram of Study Hours')
plt.xlabel('Study Hours per Day')
plt.ylabel('Frequency (Number of Students)')
plt.show()


# ==========================================
# 7. Scatter Plot: StudyHours vs PreviousScore
# ==========================================
plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df, 
    x='StudyHours', 
    y='PreviousScore', 
    hue='FinalResult', 
    palette=['red', 'green'],  # Red for Fail (0), Green for Pass (1)
    s=70, 
    alpha=0.8
)
plt.title('StudyHours vs PreviousScore (Color-coded by FinalResult)')
plt.xlabel('Study Hours')
plt.ylabel('Previous Score')
plt.legend(title='Final Result', labels=['Fail (0)', 'Pass (1)'])
plt.show()


# ==========================================
# 8. Boxplot for Attendance (Outlier Detection)
# ==========================================
plt.figure(figsize=(6, 5))
sns.boxplot(y=df['Attendance'], color='lightgreen')
plt.title('Boxplot of Attendance')
plt.ylabel('Attendance Percentage (%)')
plt.show()


# ==========================================
# 9. AssignmentsCompleted vs FinalResult Plot
# ==========================================
plt.figure(figsize=(8, 5))
sns.countplot(
    data=df, 
    x='AssignmentsCompleted', 
    hue='FinalResult', 
    palette=['salmon', 'mediumseagreen']
)
plt.title('Assignments Completed vs Final Result')
plt.xlabel('Number of Assignments Completed')
plt.ylabel('Count of Students')
plt.legend(title='Final Result', labels=['Fail (0)', 'Pass (1)'])
plt.show()


# ==========================================
# 10. SleepHours vs FinalResult (FIXED)
# ==========================================
plt.figure(figsize=(8, 5))
sns.boxplot(
    data=df, 
    x='FinalResult', 
    y='SleepHours', 
    hue='FinalResult',               # Fixed: Explicitly passed hue
    palette=['coral', 'lightskyblue'] # Fixed: Used list of colors
)
plt.title('SleepHours Distribution by Final Result')
plt.xlabel('Final Result (0 = Fail, 1 = Pass)')
plt.ylabel('Sleep Hours per Day')
plt.show()