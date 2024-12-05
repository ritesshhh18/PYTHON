# wap to extract all the integer from given list
a=[49,39,403,20,'story',8]
out=[]
for i in a:
    if type(i)==int:
     out+=[i]
print(out)