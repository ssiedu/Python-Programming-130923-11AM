num=int(input("Enter Any Number :"))
if num==0:
    print("Number is zero")
elif num>0:
    print("Positive Number")
    if num%2==0:
        print("Even number")
    else:
        print("Odd Number")
else:
    print("Negative Number")
    if num%2==0:
        print("Even number")
    else:
        print("Odd Number")
