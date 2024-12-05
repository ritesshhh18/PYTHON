#wap to check the chararcter is uppercase lower case or a no  or special character
a=input("enter the data:")
if "A"<=a<="Z":
    print("upper case")
elif "a"<=a<="z":
    print("lower case")
elif not ("A"<=a<="Z") or ("a"<=a<="z") or ("1"<=a<="9"):
    print("special character")