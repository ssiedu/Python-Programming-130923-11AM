file=open("Myfile2.txt","w")
r_no=int(input("Enter roll number :"))
name=input("Enter any Name :")
file.write(str(r_no)+"\t")
file.write(name)
file.close()
