import numpy as np

myArray1 = []
myArray2 = []
addArray=[]
mulArray=[]

x = int(input("Enter the side length of matrix: "))

print("For Matrix-1 :")
for i in range(x):
    row = []  
    for j in range(x):
        element = int(input(f"Enter element-[{i}][{j}]: "))
        row.append(element) 
    myArray1.append(row)  
    
print("For Matrix-2 :")
for i in range(x):
    row = []  
    for j in range(x):
        element = int(input(f"Enter element-[{i}][{j}]: "))
        row.append(element) 
    myArray2.append(row)  
    
myArray1 = np.array(myArray1).reshape(x,x)
myArray2 = np.array(myArray2).reshape(x,x)



print("Matrix-1 is : ")
for i in range(x):
    for j in range(x):
        print(myArray1[i][j]," ",end="")
    print()
    
print("Matrix-2 is : ")
for i in range(x):
    for j in range(x):
        print(myArray2[i][j]," ",end="")
    print()
    
for i in range(x):
    row=[]
    for j in range(x):
        row.append(myArray2[i][j]+myArray1[i][j])
    addArray.append(row) 
    
addArray = np.array(addArray).reshape(x,x)

print("Sum of Two Matrices is : ")
for i in range(x):
    for j in range(x):
        print(addArray[i][j]," ",end="")
    print()
    
for i in range(x):
    row=[]
    for j in range(x):
        element=0
        for k in range(x):
            element=element+myArray1[i][k]*myArray2[k][j]
        row.append(element)
    mulArray.append(row)
    
mulArray = np.array(mulArray).reshape(x,x)

print("Product of Two Matrices is : ")
for i in range(x):
    for j in range(x):
        print(mulArray[i][j]," ",end="")
    print()