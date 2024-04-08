expression = input("Expression: ")

try:
    x, y, z = expression.split(" ")
    x = float(x)
    z = float(z)
    if y == "":
        print(x * z)
    elif y == "+":
        print(x + z)
    elif y == "-":
        print(x - z)
    elif y == "*":
        print(x * z)
    elif y == "/":
        if z != 0:
            print(x / z)
        else:
            print("Error: Division by zero")
    else:
        print("Error: Invalid operator")
except ValueError:
    print("Error: Invalid input")