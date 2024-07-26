first = int(input("Enter first number => "))
sec = int(input("Enter second number => "))
opr = str(input("Enter Operation (+, -, *, /) => "))

if opr == "+":
    
    total = first + sec
elif opr == "-":
    total = first - sec
elif opr == "*":
    total = first * sec
elif opr == "/":
    total = first / sec
else:
    total = str("Please enter a valid operation")

print(total)