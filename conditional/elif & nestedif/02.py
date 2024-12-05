#wap to check the no is divisible by 3 the print FIZZ OR no is divisible by 5 the print buzz if both the print fizzbuzz

a=int(input("enter the no:"))
if a%3==0 and a%5==0:
    print("FIZZBUZZ")
elif a%3==0:
    print("FIZZ")
elif a%5==0:
    print("BUZZ")
