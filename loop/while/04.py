a='python programming while good'
op={}
l=a.split()
i=0
while i<len(a):
    if 'h' in  a[i]:
        op[a[i]]=1
    else:
        op[a[i]]=0
    i+=1
print(op)
    