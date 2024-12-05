#wap to check the no is 1 digit no ,2 digit no,4 digit no
a=int(input("emter the number:"))
if 0<=a<=9:
    print("1 digit no")
elif 10<=a<=99:
    print("2 digit no")
elif 100<=a<=999:
    print("3 digit no")
elif 1000<=a<=999:
    print("4 digit no")
    #optional
else :
    print("out of range")
