# Calculator

# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


def calculator():
    global num2, num1
    while True:
        try:
            num1 = float(input("What's your first number:? ").strip())
        except ValueError:
            print("Not a number, Insert your number again. ")
            continue
        break
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }
    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        operation_symbol = input("Pic an operation symbol: ")
        while operation_symbol not in ["+", "-", "*", "/"]:
            operation_symbol = input("Pic an operation symbol: ")
        while True:
            try:
                num2 = float(input("What's your next number:? ").strip())
            except ValueError:
                print("Not a number, Insert your number again. ")
                continue
            break

        calculation_symbol = operations[operation_symbol]
        answer = calculation_symbol(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer} or 'n' to restart your calculator: ").lower() == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()


if __name__ == "__main__":
    calculator()
