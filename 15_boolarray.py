import numpy as np
import random

myArray = []

x = int(input("Enter the number of rows for the array: "))
y = int(input("Enter the number of columns for the array: "))

for i in range(x):
    row = []  
    for j in range(y):
        element = round(random.random(),2)
        row.append(element) 
    myArray.append(row)  
    
myArray = np.array(myArray).reshape(x,y)

print("The Random 2D array is:")
for i in range(x):
    for j in range(y):
        print(myArray[i][j]," ",end="")
    print()
    
for i in range(x):
    for j in range(y):
        if(myArray[i][j]>0.45):
            myArray[i][j]=True
        else:
            myArray[i][j]=False
            
print("The Boolean 2D array is:")
for i in range(x):
    for j in range(y):
        print(myArray[i][j]," ",end="")
    print()