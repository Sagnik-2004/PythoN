def sort(list):
    m=len(list)
    for i in range(0,m):
        for j in range(i,m):
            if list[i]>list[j]:
                v=list[i]
                list[i]=list[j]
                list[j]=v

list1=[6,5,7,4,3]
sort(list1)
list2=[9,8,7,6,5,4,3,2,1]
sort(list2)
list3=list1+list2
sort(list3)
    
print(list3)