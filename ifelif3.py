num=int(input("Enter any number :"))
if num%5==0 and num%7==0:
    print("Divisible by Both")
elif num%5==0:
    print("Divisible by 5")
elif num%7==0:
    print("Divisible by 7")
else:
    print("Not Divisible by Both")
