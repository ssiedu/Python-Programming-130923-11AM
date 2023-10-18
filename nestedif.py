fnum=int(input("Enter First Number :"))
snum=int(input("Enter Second Number :"))
if fnum!=snum:
    if fnum>snum:
        print("Largest Number is :",fnum)
    else:
        print("Largest Number is :",snum)
else:
    print("Both Are Equal")
