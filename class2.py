class Addition:
    def getdata(self):
        self.__n1=eval(input("Enter First Number :"))
        self.__n2=eval(input("Enter Second Number :"))
    def getAdd(self):
        self.add=self.__n1+self.__n2
    def display(self):
        print("value of n1 :",self.__n1)
        print("value of n2 :",self.__n2)
        print("Addition :",self.add)

A=Addition()
A.getdata()
A.getAdd()
A.display()
#print("value of n1 :",A.__n1)

