#wap to check multivalue datatype
data=eval(input("enter the data:"))
if type(data) in [str,list,tuple,set,dict]:
    print("mvdt",data,type(data))