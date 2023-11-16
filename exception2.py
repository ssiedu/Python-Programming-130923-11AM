try:
    a=int(input("Enter First Number :"))
    b=int(input("Enter Second Number :"))
    c=a/b
    print("value of c :",c)

except TypeError:
    print("Type Mismatch")

except ValueError:
    print("Value Error Occured")

except:
    print("Some Error Occured")
