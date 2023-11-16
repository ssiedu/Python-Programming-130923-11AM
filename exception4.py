try:
    a=int(input("Enter any number upto 100 :"))
    if a>100:
        raise ValueError

except ValueError:
    print("Number is Out of range")

else:
    #print("Number is in range")
    if a%2==0:
        print("Even Number")
    else:
        print("Odd Number")
