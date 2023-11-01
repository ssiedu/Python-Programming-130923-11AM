def factorial(n):
    fact=1    
    for i in range(1,n+1):
        fact=fact*i
    print("factorial is :",fact)

n=int(input("Enter any number :"))
factorial(n)
