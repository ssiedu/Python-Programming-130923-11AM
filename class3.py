class Area:
    def input(self,Len,Bre):
        self.l=Len
        self.b=Bre
    def calArea(self):
        self.area=self.l*self.b
    def display(self):
        print("Area of rectangle :",self.area)



l=eval(input("Enter length of rectangle:"))
b=eval(input("Enter breadth of rectangle :"))
A=Area()
A.input(l,b)
A.calArea()
A.display()
    
