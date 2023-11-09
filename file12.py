import pickle
class Student:
    def __init__(self,rno=0,name=' '):
        self.rno=rno
        self.name=name
        self.s1,self.s2,self.s3=0.0,0.0,0.0
    def marks(self):
        print("Enter marks of student :")
        self.s1=eval(input("Marks of sub1 :"))
        self.s2=eval(input("Marks of sub2 :"))
        self.s3=eval(input("Marks of sub3 :"))
    def display(self):
        print("Student Information :")
        print("Roll Number :",self.rno)
        print("Name        :",self.name)
        print("Subject 1   :",self.s1)
        print("Subject 2   :",self.s2)
        print("Subject 3   :",self.s3)

'''S1=Student(101,"Ram")
S2=Student(102,"Shyam")
S1.marks()
S2.marks()
file=open("StuRecord","wb")
pickle.dump(S1,file)
pickle.dump(S2,file)
file.close()'''

file=open("StuRecord","rb")
try:
    while True:
        S=pickle.load(file)
        S.display()
except EOFError:
    file.close()



        
