from collections import Counter
d1={1:100,2:200,3:300}
d2={1:400,2:500,4:600}
'''d3={}
d3.update(d1)
d3.update(d2)
print(d3)
for i in d1.keys():
    for j in d2.keys():
        if i==j:
            d3[i]=d1[i]+d2[j]

print(d3)'''

d3=dict(Counter(d1)+Counter(d2))
print(d3)
