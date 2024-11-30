sen=input("Enter the number : ")
nes=""
for i in range(len(sen)-1,-1,-1):
    nes=nes+sen[i]
if(sen==nes):
    print(sen,"is Palindrome")
else:
    print(sen,"is Not Palindrome")