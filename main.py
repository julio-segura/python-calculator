# programa para hacer operaciones matemáticas sencillas (suma, resta, multiplicación, división)

some_text = "Welcome to the Calculatora Magnifique."
print(some_text)

# valor igual a variable (info introducida por el usario (llamada a la acción))
x = int(input("Enter the value for x: "))
y = int(input("Now enter the value for y: "))

# valor igual a info introducida por el usuario (que en este caso, ha de escoger entre las opciones proporcionadas en la llamada a la acción)

operation = input("Choose math operation +, -, *, /")

# reglas por las cuales el programa llevará a cabo las operaciones

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
