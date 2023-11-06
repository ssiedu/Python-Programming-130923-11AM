class Base:
    def getradius(self):
        self.r=eval(input("Enter radius of circle :"))



class Derive(Base):
    def calArea(self):
        self.area=3.14*self.r*self.r
    def display(self):
        print("Area of circle :",self.area)


D=Derive()
D.getradius()
D.calArea()
D.display()
    
