def Demo(*data):
    print(data)
    for i in data:
        print(i)
    print(data[1])


Demo(11,22,33,44,55)


def Demo1(**data):
    print(data)
    for i,j in data.items():
        print(i,j)
    print(data['a'])



Demo1(a=10,b=20,c=30)
