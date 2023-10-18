'''print(Select Any One :
1.Addition
2.Subtraction
3.Multiplication
4.Division)'''
while True:
    uc=input('''Do u want to continue :
1.Yes('y')
2.Exit('n')
''')
    if uc.lower()=='y' or uc=='1':
        n1=eval(input("Enter First Number :"))
        ch=input("Enter Your Choice :")
        n2=eval(input("Enter Second Number :"))
        match ch:
            case '+':
                print("{} + {} ={}".format(n1,n2,n1+n2))
            case '-':
                print("{} - {} ={}".format(n1,n2,n1-n2))
            case '*':
                print("{} * {} ={}".format(n1,n2,n1*n2))
            case '/':
                print("{} / {} ={}".format(n1,n2,n1/n2))
            case _:
                print("Please Enter Valid Choice ")
    else:
        break;
