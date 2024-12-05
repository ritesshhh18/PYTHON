#wap take a list that list should act like set
I=[1,3,5,2,5,7,8,3,6,3,3]
op=[]
i=0

while i<len(I):
    if I[i] not in op:
        op+=[I[i]]
    i+=1
print(op)