while 1:
    num1=float(input("Enter the first number:"))
    num2=float(input("Enter the second number:"))

    op=input("Enter the operator (+,-,*,/,// or %) :")

    if  (op=='/' or op=='//' or op=='%') and num2==0:
        print("Error! Denominator can not be zero.")

    elif op=='+':
        print(num1+num2)

    elif op=='-':
        print(num1-num2)

    elif op=='*':
        print(num1*num2)

    elif op=='/':
        print(num1/num2)

    elif op=='//':
        print(num1//num2)

    elif op=='%':
        print(num1%num2)

    else:
        print("Invalid Operator!!")