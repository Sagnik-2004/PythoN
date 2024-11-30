#Write a python program to find the area of a  triangle
import math
a=int(input("Enter side-1 : "))
b=int(input("Enter side-2 : "))
c=int(input("Enter side-3 : "))
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area : ",str(area))