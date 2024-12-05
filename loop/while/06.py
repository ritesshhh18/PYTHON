a='hai hello'.split()
op={}
i=0
while i<len(a):
    op(a[i])=[a[i],len(a[i])*2, a[i][::-1]+str(len(a[i]))]
print(op)
 