import pandas as pd

# Create a Pandas Series
data = pd.Series([100, 200, 300, 400, 500], index=['a', 'b', 'c', 'd', 'e'])

print("Original Series:")
print(data)

# Convert Series to DataFrame with the index as a column
df = data.reset_index()

# Rename columns for clarity
df.columns = ['Index', 'Value']

print("\nConverted DataFrame:")
print(df)
