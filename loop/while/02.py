a="(()))(())"
c=0
c1=0
i=0
while i<len(a):
    if a[i]=='(':
        c+=1
    else:
        c1+=1
    i+=1
print(abs(c-c1))