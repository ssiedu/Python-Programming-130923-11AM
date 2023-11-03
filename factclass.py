class Factorial:
    def getNum(self):
        self.n=int(input("Enter any number :"))
    def calFact(self):
        f=1
        for i in range(1,self.n+1):
            f=f*i
        print("Factorial of a number :",f)

F=Factorial()
F.getNum()
F.calFact()
