print("Enter the first number: ")

num1 = int(input())

print("Enter the second number: ")

num2 = int(input())

print("Choose the operation (+,-,*,/): ")

operation = input()

match operation:
    case "+":
     result = num1 + num2
     print(f"The result is {result}")

    case "-":
     result = num1 - num2
     print(f"The result is {result}")

    case "*":
      result = num1 * num2
      print(f"The result is {result}")

    case "/":
       result = num1 / num2
       print(f"The result is {result}")
