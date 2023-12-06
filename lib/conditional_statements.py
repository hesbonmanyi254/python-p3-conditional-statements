# conditional_statements.py

def calculator(operator, operand1, operand2):
    # Your calculator logic here
    if operator == "+":
        result = operand1 + operand2
    elif operator == "-":
        result = operand1 - operand2
    elif operator == "*":
        result = operand1 * operand2
    elif operator == "/":
        result = operand1 / operand2
    else:
        print("Invalid operator")
        return

    print(f"Result: {result}")

# Example usage
calculator("+", 1, 1)
