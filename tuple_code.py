a=()					# empty tuple
b=(2,)					# tuple with single element  ** must put ,
c=(2, 4, 6, 7, 8)			# immutable
mixed = (2, 'A', (1,3, 4), 7.56)	# int, string,tuple, float ; tuple within it i,e nested tuple
tl_lt= (1,2,3,[4,5,6],(7,8),10)

print (a)
print (b)
print (mixed)
print (mixed[2])
print (mixed[2][2])
print (tl_lt[4][1])
print (tl_lt[3][:2])			# in third elemnt i,e in list[] up to location <2  this is called SLICE
print (tl_lt[3][1:])			# in list[] from location 1

tt= tl_lt[3][:2]
print(tt, type(tt))			# type list copy
tt2= list(tl_lt[3][:2])
print(tt2, type(tt2))

tu = tl_lt[0:3]
print(tu, type(tu))			# type tuple copy
tu2 = tuple(tl_lt[0:3])
print(tu2, type(tu2))

print (tl_lt[:4],'\t', tl_lt[4:])
print (type('A')) 
print (type((2)),' ', type(b))		# clas int , class tuple  --- so (2) is not a tuple

lt1=[8,7,6,5,4,'A']			# list mutable
print (lt1[:3],'\t',lt1[3:])
print (lt1[2:5])			# from location 2 to < 5

	# List containing different type of objects 
lt2=[5,6,(1,2,3),[4,9]]
print (lt2[2],'\t',lt2[:2],'\t',lt2[3])
print (type(lt2),'\t',type(lt2[2]),'\t',type(lt2[3]),'  ',type(lt2[1]))

	# List within a list, merging two lists 
lt3 = ['ab','bc','cd']
lt4 = ['bb','cc','dd']
lt5 = [['ab','bc','cd'],['bb','cc','dd']]
lt6 = [lt3,lt4]
print (lt5==lt6)		# Equality checking of two lists

str1='klp'				# class 'str' for string immutable
print (str1)
print (str1[1])
str1 = 'rtp'
print (str1, type(str1))







