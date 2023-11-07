class Base:
    def getNum(self):
        self.num1=eval(input("Enter First Number :"))
        self.num2=eval(input("Enter Second Number :"))

class Parent(Base):
    def calProduct(self):
        self.pro=self.num1*self.num2


class child(Parent):
    def display(self):
        print("product of two numbers :",self.pro)


C=child()
C.getNum()
C.calProduct()
C.display()
    
