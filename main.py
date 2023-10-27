# Simple Python app to perform mathematical operations (add, substract, multiply, division)

some_text = "Welcome to the Calculatora Magnifique."
print(some_text)

# We ask the user to imput two numbers
x = int(input("Enter the value for x: "))
y = int(input("Now enter the value for y: "))

# We ask the user to choose the math operation that they want to perform

operation = input("Choose math operation +, -, *, /")

# Rules that tell the program which operations to perform

if operation == "+":
    print(x + y)
elif operation == "-":
    print(x - y)
elif operation == "*":
    print(x * y)
elif operation == "/":
    print(x / y)
else:
    print("You did not provide the correct math operation.")
