while True:
    try:
        a = float(input("Введіть перше число: "))
        b = float(input("Введіть друге число: "))
        operacion = input("Введіть операцію (+, -, /, *, mod, pow, div): ")
        if operacion not in ["+", "-", "/", "*", "mod", "pow", "div"]:
            print("Недопустима операція")
            continue
        if operacion == "+":
            result = a + b
        elif operacion == "-":
            result = a - b
        elif operacion == "*":
            result = a * b
        elif operacion == "/":
            if b == 0:
                raise ZeroDivisionError
            result = a / b
        elif operacion == "mod":
            if b == 0:
                raise ZeroDivisionError
            result = a % b
        elif operacion == "pow":
            result = a ** b
        elif operacion == "div":
            if b == 0:
                raise ZeroDivisionError
            result = a // b
        print(f"{a} {operacion} {b} = {result}")
    except ValueError:
        print("Недопустиме значення числа")
    except ZeroDivisionError:
        print("Division by zero!")
    else:
        break