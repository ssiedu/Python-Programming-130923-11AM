for i in range(65,91):
    print(chr(i),end=" ")
print()

for i in range(ord('a'),ord('z')+1):
    print(chr(i),end=" ")

print()

i=ord('z')
while i>=ord('a'):
    print(chr(i),end=" ")
    i=i-1
