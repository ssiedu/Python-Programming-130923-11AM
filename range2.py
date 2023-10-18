from itertools import chain
var=chain(range(5),range(10,20),range(5,51,5))
for i in var:
    print(i,end=" ")
