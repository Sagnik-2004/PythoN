myArray = [1,None,2,None,'A',True,213,None,420,False,None,'Sagnik']

print("The Array is : ",myArray)

c=0

for i in range(len(myArray)):
    if myArray[i]==None:
        c=c+1

print("Number of Null Elements : ",c)