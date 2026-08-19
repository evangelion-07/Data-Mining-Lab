import pandas as pd

data = {
    'Year': [2024, 2024, 2024, 2025, 2025, 2025],
    'Product': ['Laptop', 'Mobile', 'Laptop', 'Mobile', 'Laptop', 'Mobile'],
    'Location': ['Hyderabad', 'Hyderabad', 'Chennai',
                 'Chennai', 'Hyderabad', 'Chennai'],
    'Sales': [50000, 30000, 45000, 35000, 60000, 40000]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

cube = pd.pivot_table(
    df,
    values='Sales',
    index='Product',
    columns=['Year', 'Location'],
    aggfunc='sum',
    fill_value=0
)

print("\nData Cube:")
print(cube)

print("\nRoll-Up (Year and Product):")
rollup = df.groupby(['Year', 'Product'])['Sales'].sum()
print(rollup)

print("\nDrill-Down:")
drilldown = df.groupby(
    ['Year', 'Location', 'Product']
)['Sales'].sum()
print(drilldown)

print("\nSlice (Year = 2025):")
slice_data = df[df['Year'] == 2025]
print(slice_data)

print("\nDice:")
dice_data = df[
    (df['Product'].isin(['Laptop', 'Mobile'])) &
    (df['Location'].isin(['Hyderabad', 'Chennai']))
]
print(dice_data)
