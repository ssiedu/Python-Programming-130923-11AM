file=open("Myfile4.txt","w")
n=int(input("How many Students info do u want to enter:"))
for i in range(n):
    r_no=int(input("Enter Roll Number :"))
    name=input("Enter Name :")
    per=eval(input("Enter Percentage"))
    data= str(r_no)+"\t"+name+"\t"+str(per)+"\n"
    file.write(data)

file.close()
