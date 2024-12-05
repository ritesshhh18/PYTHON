a=['home.py','google.com','yahoo.in','gmail.com','index.html']
op={}
for ch in a:
    c=ch.split('.')
    if c[1] in op:
        op[c[1]]+=[c[0]]
    else:
      op[c[1]]=[c[0]]
print(op)