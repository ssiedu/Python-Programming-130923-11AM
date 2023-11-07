class Parent1:
    def getAmount(self):
        self.p=eval(input("Enter Principle Amount :"))


class Parent2:
    def getRate(self):
        self.r=eval(input("Enter Rate of Interest :"))


class Parent3:
    def getTime(self):
        self.t=eval(input("Enter time in year :"))


class Child(Parent1,Parent2,Parent3):
    def calSI(self):
        self.si=(self.p*self.r*self.t)/100
        self.total=self.si+self.p
        print("Simple Interest :",self.si)
        print("Total Amount :",self.total)


C=Child()
C.getTime()
C.getAmount()
C.getRate()
C.calSI()







        
