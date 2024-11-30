myarray=[]

x=int(input("Enter the length of array : "))

for i in range(x):
    myarray.append(int(input(f"Enter {i}th element : ")))
    
print("The input array is : ",myarray)

array2=[]

for i in range(x):
    m=myarray[i]
    if m not in array2:
        c=0    
        array2.append(m)
        for j in range(x):
            if m==myarray[j]:
                c=c+1
        print(f"{m} is present {c} times")