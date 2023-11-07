class Base:
    def __init__(self):
        self.l=eval(input("Enter length of rectangle :"))
        self.b=eval(input("Enter breadth of rectangle :"))


class Parent1(Base):
    def calRArea(self):
        self.rArea=self.l*self.b



class Parent2:
    def getRadius(self):
        self.r=eval(input("Enter Radius of circle :"))
    def calCArea(self):
        self.cArea=3.14*self.r*self.r

class child(Parent1,Parent2):
    def Display(self):
        print("Area of rectangle :",self.rArea)
        print("Area of circle :",self.cArea)


C=child()
#C.getNum()
C.calRArea()
C.getRadius()
C.calCArea()
C.Display()




    





        
