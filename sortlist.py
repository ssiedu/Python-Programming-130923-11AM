L1=[]
n=int(input("How many items do u want to enter:"))
for i in range(n):
    num=int(input("Enter Number :"))
    L1.append(num)

print("List Is :")
print(L1)
L1.sort()
print("Sorted List :")
print(L1)
L1.sort(reverse=True)
print("Reverse List :")
print(L1)
