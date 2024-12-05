#wap to extract the last value of the given list and it should be string and lenght should be more than 3
a=eval(input("enter the data:"))
if type(a[-1])==str and len(a[-1])>3:
    print("yes")