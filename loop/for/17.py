a=['home.py','google.com','yahoo.in','gmail.com','index.html']
op=[]
# for ch in a:
#     i=ch.index(".")
#     op+=[ch[i+1:]]
# print(op)
    
for i in a:
    a=i.split('.')
    op+=[a[1]]
print(op)