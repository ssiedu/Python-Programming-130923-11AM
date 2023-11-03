flag=0
n=int(input("Enter Any Number :"))
for i in range(2,(n//2+1)):
    if n%i==0:
        flag=1
        break;

if flag==0:
    print("Prime Number")
else:
    print("Not prime")
    
