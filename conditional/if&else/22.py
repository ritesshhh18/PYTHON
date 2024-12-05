#wap to check the data is svdt or mvdt
data=eval(input("enter the data"))
if type(data) in [str,list,tuple,set,dict]:
    print("data is mvdt")
else :
    print("data is svdt")