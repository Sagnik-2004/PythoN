import numpy as np

myArray = []

x = int(input("Enter the number of rows for the array: "))
y = int(input("Enter the number of columns for the array: "))

for i in range(x):
    row = []  
    for j in range(y):
        element = int(input(f"Enter element-[{i}][{j}]: "))
        row.append(element) 
    myArray.append(row)  

myArray = np.array(myArray).reshape(x,y)
print("The input 2D array is:")

for i in range(x):
    for j in range(y):
        print(myArray[i][j]," ",end="")
    print()


for i in range(y):
    print(f"column:{i}")
    for j in range(x):
        print(myArray[j][i])
    print()