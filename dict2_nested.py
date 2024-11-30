child1 = {"name":("Emil","hgt"),"year":2004}
child2 = {"name":"Tobias","year":2007}
child3 = {"name":"Linus","year":2011}

myfamily = {"child1":child1, "child2" : child2,"child3" : child3}
print(myfamily)
print(myfamily["child2"]["name"])

sampleDict = {
    "class": {
        "student": {
            "name": "Arnab",
            "marks": {
                "physics": 70,
                "computer": [80,90]
            } } } }

print(sampleDict)
MarksDict = sampleDict["class"]["student"]["marks"]
for marks in (MarksDict["computer"]):
    print(marks," ..")

tup=[("dw","aa"),("bc","tr"),("de","sd")]
# print(sorted(tup))
k=len(tup)
temp=list([])
for i in range(0,k):
    temp+=list((tup[i][1],))
#    print(tup[i][1])
print(temp)
temp.sort()
tup2=list((tup[i]) for m in temp
                  for i in range(0,k)
                      if(tup[i][1]==m))

print(tup2," ",type(tup2)," ",type(tup2[0]))
# tup.sort()
# print(tup)