def calc(a,b,opt):
    if opt==1:
        return a+b
    elif opt==2:
        return a-b
    elif opt==3:
        return a*b
    elif opt==4:
        try:
            return a/b
        except Exception:
            print("zero division error second number can't be zero")
    else:
        print("Choose correct choice for calculation")


a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print('''Select an option
1.Addition
2.Subtraction
3.Multiplication
4.Division''')
opt=int(input())
result=calc(a,b,opt)
print("Answer is :",result)