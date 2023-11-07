class Base:
    def getNum(self):
        self.n1=eval(input("Enter First Number :"))
        self.n2=eval(input("Enter Second Number :"))


class child1(Base):
    def calAdd(self):
        self.add=self.n1+self.n2
        print("Addition :",self.add)


class child2(Base):
    def calMul(self):
        self.mul=self.n1*self.n2
        print("Multiplication :",self.mul)

class child3(Base):
    def calDiv(self):
        self.div=self.n1/self.n2
        print("Division :",self.div)


c1=child1()
c1.getNum()
c1.calAdd()
c2=child2()
c2.getNum()
c2.calMul()
c3=child3()
c3.getNum()
c3.calDiv()








        
