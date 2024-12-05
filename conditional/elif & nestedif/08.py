#wap to check the given character is vowel or consonent but prove it by nested
a=input("enter the char:")
if "A"<=a<="Z" or "a"<=a<="z":
    if a in "AEIOUaeiou":
        print("vowel")
    else:
        print("consonent")
else:
    print("not a character")