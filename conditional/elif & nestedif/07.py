#wap to check the data is mvdt but its lenght should be greater than 4
a=eval(input("enter the data:"))
if type(a) in [str,list,tuple,set,dict]:
    if len(a)>4:
        print("mvdt and greater than 4")
    else :
        print("mvdt but less than 4")
else:
    print("not mvdt")