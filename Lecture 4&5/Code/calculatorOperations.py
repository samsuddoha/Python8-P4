
num1,num2=map(float,input("Enter two numbers by space seperator: ").split())

addition=num1+num2
multiply=num1*num2

#subtraction
if num1>num2:
    subtract=num1-num2
else:
    subtract=num2-num1

#Division
if num2==0:
    print("Infinite")
else:
    division=num1/num2

print(f"The summation of {num1} and {num2} is: {addition}")
print(f"The subtraction of {num1} and {num2} is: {subtract}")
print(f"The multiplication of {num1} and {num2} is: {multiply}")
print(f"The division of {num1} and {num2} is: {division}")