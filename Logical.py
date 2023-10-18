n1=int(input("Enter First number :"))#10
n2=int(input("Enter Second Number :"))#20

print("And :",n1>n2 and n1!=n2)#False
print("Or  :",n1<n2 or n1==n2)#True
print("Not :",not(n1<n2))#False
print("And Not :",not(n1==n2 and n1>n2))#True
print("Or Not  :",not(n1<n2 or n1!=n2))#False
print("AND OR NOT :",not((n1>n2 and n1==n2)or not(n1)))#True
