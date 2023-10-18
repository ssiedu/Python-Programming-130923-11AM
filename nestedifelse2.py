num=int(input("Enter Any Number :"))
if num==0:
    print("Number is Zero")
elif num%2==0:
    print("Even Number")
    if num>0:
        print("Positive Number")
    else:
        print("Negative Number")
else:
    print("Odd Number")
    if num>0:
        print("Positive Number")
    else:
        print("Negative Number")
