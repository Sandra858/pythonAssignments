#get user inputs
num1 = float(input("Enter a number:"))
num2 = float(float(input("Enter the second number:")))

Operation = input("Enter an operation(+,-,*,/):")

#Calculation
if Operation == "+":
    result = num1+num2
    print(f"{num1} + {num2} = {result}")
elif Operation == "-":
    result = num1- num2
    print(f"{num1} - {num2} ={result}")

elif Operation == "*":
    result = num1 * num2 
    print(f"{num1} *{num2} ={result}")
elif   Operation == "/":
    if num2 != 0:
        result = num1/num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed")
else:
    print('Invalid operation. Please enter one of +, -, *, or /.')        
    
    