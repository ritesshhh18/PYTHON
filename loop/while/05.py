a='hello'
b='bye'
op=""
i=0
while i<len(a) or i<len(b):
    if i<len(a):
        op+=a[i]
    if i<len(b):
        op+=b[i]
    i+=1
print(op)
