def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
    
var=fact(5)
print("factorial of a number is :",var)
