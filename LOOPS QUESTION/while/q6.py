#  WAP TO EXTRACT ALL THE UPPERCASE ALPHABET FROM GIVEN STRING
a=input("enter the string :")
i=0
out=""
while i<len(a):
    if "A"<=a[i]<="Z":
     out+=a[i]
    i+=1
print(out)