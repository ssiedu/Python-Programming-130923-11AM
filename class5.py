class Series:
    def input(self):
        self.n=int(input("Enter Stop Limit:"))
    def printSeries(self):
        i=1
        while i<=self.n:
            print(i,end=" ")
            i=i+1
        #for i in range(1,self.n+1):
            #print(i,end=" ")


S=Series()
S.input()
S.printSeries()
