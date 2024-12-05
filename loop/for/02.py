#wap to search for a number x in this tuple using loop
a=(1,4,9,16,25,36,49,64,81,100,49)
x=49

index=0
for el in a:
    if (el==x):
        print("number found at index",index)
        break
    index+=1
        