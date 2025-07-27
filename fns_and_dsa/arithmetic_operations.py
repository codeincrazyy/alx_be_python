def perform_operaton(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtrack":
        return num1 - num2
    elif operation == "multply":
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return num1 / num2
    else:
        return "error: invalid operation"
      