class Addition:
    def __init__(self):
        self.n1=eval(input("Enter First Number :"))
        self.n2=eval(input("Enter Second Number :"))
    def calAdd(self):
        self.add=self.n1+self.n2
        print("Addition is :",self.add)

A=Addition()
A.calAdd()
