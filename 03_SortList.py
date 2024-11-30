myList=[7,1,6,3,5,2,9,4]

m=len(myList)

for i in range(0,m):
    for j in range(i,m):
        if myList[i]>myList[j]:
            v=myList[i]
            myList[i]=myList[j]
            myList[j]=v

print(myList)
        
        