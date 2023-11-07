class Base:
    def getData(self):
        print("This is Base Class Function")


class Derive(Base):
    def getData(self):
        #Base.getData(self)
        super().getData()
        print("This is Derive Class Function")


D=Derive()
D.getData()
#D.getData()
