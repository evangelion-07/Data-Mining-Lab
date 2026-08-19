import pandas as pd

data = {
    
    'City': ['Hyderabad', 'Chennai'],
    'Product': ['Laptop', 'Mobile'],
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

city_to_country = {
    'Hyderabad': 'India',
    'Chennai': 'India'
}

product_to_category = {
    'Laptop': 'Electronics',
    'Mobile': 'Electronics'
}

df['Country'] = df['City'].map(city_to_country)
df['Category'] = df['Product'].map(product_to_category)



result = df[['Country', 'Category']]

result = result.value_counts().reset_index(name='Count')

print("\nGeneralized Data:")
print(result)
