try:
    print("Try Block")
    a=int(input("Enter First Number :"))
    b=int(input("Enter Second Number :"))
    c=a/b

except:
    print("Except Block")
    print("Some Error Occured")

else:
    print("Else block")
    print("Value of c :",c)

finally:
    print("Finally Block")
    print("Thank You")
