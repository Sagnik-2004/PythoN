print("Loop 1")
t = (1,2,3,4,5)
for i in t:
    print(i)
    
print("Loop 2")  
for i in range(1,5):
    print(i)

def new_func():
    print("Loop 3")
    for i in range(1,6):
        print(i)

new_func()
    
print("Loop 4")  
for i in range(1,5,2):
    print(i)