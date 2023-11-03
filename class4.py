class PosNeg:
    def getdata(self):
        self.num=eval(input("Enter Any Number :"))
    def checkInput(self):
        if self.num>0:
            print("Positive number")
        elif self.num==0:
            print("Number is Zero")
        else:
            print("Negative Number")

P=PosNeg()
P.getdata()
P.checkInput()
