class Fib:
    def getdata(self):
        self.n=int(input("Enter Limit :"))
        self.x=0
        self.y=1
    def printSeries(self):
        print(self.x)
        print(self.y)
        i=2
        while i<self.n:
            z=self.x+self.y
            print(z)
            self.x=self.y
            self.y=z
            i=i+1
    

F=Fib()
F.getdata()
F.printSeries()
