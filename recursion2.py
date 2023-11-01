def SumSeries(n):
    if n==1:
        return 1
    else:
        return n+SumSeries(n-1)


n=int(input("Enter any number :"))
var=SumSeries(n)
print("sum of series :",var)
