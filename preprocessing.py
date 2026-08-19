import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Data Processing Techniques:
# 1. Data Cleaning
# 2. Data Transformation - Normalization
# 3. Data Integration

# Student data
student_data = pd.DataFrame({
    "ID": [1, 2, 3, 4, 5],
    "Name": ["Alice", "Bob", "John", "David", "Eva"],
    "Age": [20, 21, None, 23, 22],
    "Marks": [85, 90, 78, None, 88]
})

# Department data
department_data = pd.DataFrame({
    "ID": [1, 2, 3, 4, 5],
    "Department": ["CSE", "ECE", "ECE", "MECH", "CIVIL"]
})

# Display original student data
print("Original Student Database:")
print(student_data)

# Data Cleaning
print("\nAfter Data Cleaning:")

student_data["Name"] = student_data["Name"].fillna("Unknown")

student_data["Age"] = student_data["Age"].fillna(
    student_data["Age"].mean()
)

student_data["Marks"] = student_data["Marks"].fillna(
    student_data["Marks"].mean()
)

print(student_data)

# Data Transformation - Normalization
print("\nAfter Normalization:")

scaler = MinMaxScaler()

student_data["Marks_Normalized"] = scaler.fit_transform(
    student_data[["Marks"]]
)

print(student_data)

# Data Integration
print("\nAfter Data Integration:")

merged_data = pd.merge(
    student_data,
    department_data,
    on="ID"
)

print(merged_data)