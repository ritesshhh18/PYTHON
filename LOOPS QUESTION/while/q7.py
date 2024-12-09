# extract all the special character
a=input("enter the string :")
i=0
str=""
c=("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890")
while i<len(a):
    if a[i] not in c :
        str+=a[i]
    i+=1
print(str)