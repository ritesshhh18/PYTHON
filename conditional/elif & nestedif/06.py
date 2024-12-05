#wap to check to check no is divisible by 5 but it should be even
a=int(input("enter the no:"))
if a%5==0:
    if a%2==0:
        print("div by 5 and even")
    else:
        print("div by 5 but odd")
else:
    print("not div by 5")