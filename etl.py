import pandas as pd

data = {
    'Name': ['John', 'Alice', 'Bob', 'David'],
    'Age': [20, 22, 21, 23],
    'Marks': [85, 90, 75, 80]
}

df = pd.DataFrame(data)

print("Extracted Data:")
print(df)

df['Final_Marks'] = df['Marks'] + 5

df.to_csv('student_data.csv', index=False)

print("\nTransformed and Loaded Data:")
print(df)
