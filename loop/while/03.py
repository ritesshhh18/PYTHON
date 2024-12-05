#wap to check a number is perfect number
a=int(input("enter the number"))
i=1
s=0
while i<a:
    if a%i==0:
        s+=i
    i+=1
if s==a:
    print("perfect")
else:
    print("not perfect")