import pandas as pd

# Original DataFrame
df1 = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

# Replacement DataFrame
df2 = pd.DataFrame({
    'A': [10, 45, 30],
    'B': [40, 50, 66],
    'C': [12, 80, 90]
})

print("Original DataFrame-1:")
print(df1)

print("\nOriginal DataFrame-2:")
print(df2)

# Update `df1` with values from `df2`
df1.update(df2)

print("\nUpdated DataFrame-1:")
print(df1)
