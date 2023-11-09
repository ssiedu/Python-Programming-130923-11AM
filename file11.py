import pickle
file=open("Myfile8","wb")
list1=[10,11,12,13,14,15]
pickle.dump(list1,file)
file.close()

file=open("Myfile8","rb")
data=pickle.load(file)
print(data)
file.close()
