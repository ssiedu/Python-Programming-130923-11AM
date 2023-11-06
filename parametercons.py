class Addition:
    def __init__(self,x,y):
        self.n1=x
        self.n2=y
    def calAdd(self):
        self.add=self.n1+self.n2
        print("Addition is :",self.add)



a=eval(input("Enter the value of a :"))
b=eval(input("Enter the value of b :"))

A=Addition(a,b)
A.calAdd()
