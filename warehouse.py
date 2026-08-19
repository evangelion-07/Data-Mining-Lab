import pandas as pd

# Data Cube Construction - OLAP Operations

data = {
    "Year": [2024, 2024, 2024, 2025, 2025, 2025],
    "Product": ["Laptop", "Mobile", "Laptop", "Mobile", "Laptop", "Mobile"],
    "Location": ["Hyderabad", "Hyderabad", "Chennai",
                 "Chennai", "Hyderabad", "Chennai"],
    "Sales": [50000, 30000, 75000, 35000, 60000, 40000]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Data Cube
cube = pd.pivot_table(
    df,
    values="Sales",
    index="Product",
    columns=["Year", "Location"],
    aggfunc="sum",
    fill_value=0
)

print("\nData Cube:")
print(cube)

# --------------------------------
# OLAP Operation 1: Roll-Up
# --------------------------------

print("\nRoll-Up (Year and Product):")

rollup = df.groupby(
    ["Year", "Product"]
)["Sales"].sum()

print(rollup)

# --------------------------------
# OLAP Operation 2: Drill-Down
# --------------------------------

print("\nDrill-Down:")

drill_down = df.groupby(
    ["Year", "Location", "Product"]
)["Sales"].sum()

print(drill_down)

# --------------------------------
# OLAP Operation 3: Slice
# --------------------------------

print("\nSlice (Year = 2025):")

slice_data = df[df["Year"] == 2025]

print(slice_data)

# --------------------------------
# OLAP Operation 4: Dice
# --------------------------------

print("\nDice:")

dice_data = df[
    (df["Product"].isin(["Laptop", "Mobile"])) &
    (df["Location"].isin(["Hyderabad", "Chennai"]))
]

print(dice_data)