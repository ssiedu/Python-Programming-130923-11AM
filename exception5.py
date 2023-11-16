try:
    a=int(input("Enter any number :"))
    assert a%2==0

except:
    print("Not a Valid Input")

else:
    rec=1/a
    print("Reciprocal of a number :",rec)
