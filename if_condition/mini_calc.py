num1=int(input("enter the first number: "))
num2=int(input("enter the second number: "))
operator=input("enter the operation(+,-,*,/,%,//,**) you want: ")
if operator=="+":
   print("result",num1+num2)
elif operator=="-":
   print("result",num1-num2)
elif operator=="*":
   print("result",num1*num2)
elif operator=="/":
   print("result",num1/num2)  
elif operator=="//":
    if num2!=0:
       print("result",num1//num2)
    else:
       print("cannot divide by zero")
elif operator=="%":
   print("result",num1%num2)
elif operator=="**":
   print("result",num1**num2)
else:
   print("invalid operator")