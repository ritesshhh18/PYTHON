#wap to print to print highest no among four no.
# a=int(input("enter the 1st no:"))
# b=int(input("enter the 2nd no:"))
# c=int(input("enter the 3rd no:"))
# d=int(input("enter the 4th no:"))
# if a>b and a>c and a>d:
#     print("highest no is",a)
# elif b>a and b>c and b>d:
#     print("highest no is",b)
# elif c>a and c>b and c>d:
#     print("highest no is",c)
# elif d>a and d>b and d>c:
#     print("highest no is",d)
a,b,c,d = eval(input("enter the no:"))
if a>b and a>b and a>c and a>d:
    print(a)
elif b>c and b>d:
    print(b)
elif c>d:
    print(c)
else :
    print(d)