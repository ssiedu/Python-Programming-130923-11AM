from multipledispatch import dispatch

@dispatch(int,int)
def Add(fnum,snum):
    result=fnum+snum
    print("Addition of two int value :",result)

@dispatch(int,float)
def Add(fnum,snum):
    result=fnum+snum
    print("Addition of two diff value :",result)

@dispatch(float,float)
def Add(fnum,snum):
    result=fnum+snum
    print("Addition of float value :",result)

@dispatch(int,int,int)
def Add(fnum,snum,tnum):
    result=fnum+snum+tnum
    print("Addition of Three int value :",result)

@dispatch(str,str)
def Add(fnum,snum):
    result=fnum+snum
    print("Addition of str value :",result)



Add(2,3,4)
Add(10,20)
Add(2,3.4)
Add(2.2,3.2)
Add("Hello","World")





    
