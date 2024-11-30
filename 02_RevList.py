myList=["Pen","Book","Scale","Pencil", "Page"]

print("Original List :",myList)  

m=len(myList)

for i in range(0,(m-1)//2):
    x=myList[i]
    myList[i]=myList[m-i-1]
    myList[m-i-1]=x

print("Reversed List :",myList)    