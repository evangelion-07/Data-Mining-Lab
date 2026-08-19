import pandas as pd
from sklearn.preprocessing import MinMaxScaler
student_data = pd.DataFrame({
    "ID": [1, 2, 3, 4, 5],
    "Name": ["Alice", "Bob", "John", "David", "Eva"],
    "Age": [20, 21, None, 23, 22],
    "Marks": [85, 90, 78, None, 88]
})

department_data = pd.DataFrame({
    "ID": [1, 2, 3, 4, 5],
    "Department": ["CSE", "ECE", "ECE", "MECH", "CIVIL"]
})

print("Original Student Database:")
print(student_data)

print("\nAfter Data Cleaning:")

student_data["Name"] = student_data["Name"].fillna("Unknown")

student_data["Age"] = student_data["Age"].fillna(
    student_data["Age"].mean()
)

student_data["Marks"] = student_data["Marks"].fillna(
    student_data["Marks"].mean()
)

print(student_data)

print("\nAfter Normalization:")

scaler = MinMaxScaler()

student_data["Marks_Normalized"] = scaler.fit_transform(
    student_data[["Marks"]]
)

print(student_data)

print("\nAfter Data Integration:")

merged_data = pd.merge(
    student_data,
    department_data,
    on="ID"
)

print(merged_data)
