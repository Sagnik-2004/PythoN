import pandas as pd
import numpy as np

data = {
    "Column1": [1, None, 2, None, "A"],
    "Column2": [True,"Java", None, 420, False],
    "Column3": [None, "Sagnik", None, None, "Python"],
    "Column4": [None, 234234234, None, np.nan, "Pal"],
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

c=0

for i in range(len(df)):
    for j in range(len(df.columns)):
        if df.iloc[i,j]==None:  
            c = c+1
            
print("Number of Null Elements : ",c)