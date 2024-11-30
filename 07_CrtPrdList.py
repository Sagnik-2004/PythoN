lst1=['1','2','3']
lst2=['A','B','C']
lst3=[]

m=len(lst1)
n=len(lst2)

for i in range(m):
    for j in range(n):
        lst3=lst3+[lst1[i]+lst2[j]]
        
print(lst3)

