import pandas as pd

data = {
    'Name': ['John', 'Alice', 'Bob', 'David'],
    'City': ['Hyderabad', 'Chennai', 'Mumbai', 'Delhi'],
    'Product': ['Laptop', 'Mobile', 'Laptop', 'Mobile'],
    'Age': [21, 22, 35, 40]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

city_to_country = {
    'Hyderabad': 'India',
    'Chennai': 'India',
    'Mumbai': 'India',
    'Delhi': 'India'
}

product_to_category = {
    'Laptop': 'Electronics',
    'Mobile': 'Electronics'
}

df['Country'] = df['City'].map(city_to_country)
df['Category'] = df['Product'].map(product_to_category)

def age_group(age):
    if age <= 25:
        return 'Young'
    else:
        return 'Adult'

df['Age_Group'] = df['Age'].apply(age_group)

result = df[['Country', 'Category', 'Age_Group']]

result = result.value_counts().reset_index(name='Count')

print("\nGeneralized Data:")
print(result)
