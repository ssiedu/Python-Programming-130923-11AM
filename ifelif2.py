char=input("Enter any character :")
if char>='A' and char <='Z':
    print("Upper Case")
elif char>='a' and char<='z':
    print("Lower Case")
elif char>='0' and char<='9':
    print("Digit")
else:
    print("Special Symbol")
