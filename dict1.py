dict1 = {1:"I",2:"am",3:"a",4:"man"}
print(dict1)
del(dict1[2])	# To delete an entry with key value
print(dict1)
dict1[2]="Was"	# To modify value of specified key
dict1[5]="Oh!"
print(dict1)
print(list(dict1))	#  To return a list of all keys using list function
		#  Not using function
for i in dict1:
	print(i)

for i,j in dict1.items():
	print(i,j)

print(dict1.keys())
print(dict1.values())
wq= dict1.keys()
print(type(wq))
for i in wq:
	print(i)
			# Using dict() constructor
std = dict(name = "Arun", age = 20, country = "India")
print(std)
		# copy dictionary
std2= dict(std)
print(std2)
dict2={8:"g", 9:"kj"}
std3=dict({"dict1":dict1,"dict2":dict2})
std4 ={"dict1":dict1,"dict2":dict2}
print(std3," ",type(std3))
print(std4," ",type(std4))
