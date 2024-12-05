a='abqstz'
op=""
for i in a:
    if ord(i)==122:
        op+="a"
    else:
        op+=chr(ord(i)+1)
print(op)