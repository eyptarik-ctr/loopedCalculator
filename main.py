ansver = True
raund = 1

while ansver:
    if raund == 1:
        s1 = int(input("Enter first number: "))
        process = input("Choose operation (+, -, *, /): ")
        s2 = int(input("Enter second number: "))
    elif raund == 2:
        s1 = result
        process = input("Choose operation (+, -, *, /): ")
        s2 = int(input("Enter second number: "))

    def sumFun(a, b):
        return a + b

    def divFun(a, b):
        if b != 0:
            return a / b
        else:
            print("Error: Division by zero")
            return None

    def minusFun(a, b):
        return a - b

    def multiplyFun(a, b):
        return a * b

    # Perform the selected operation
    if process == "+":
        result = sumFun(s1, s2)
    elif process == "/":
        result = divFun(s1, s2)
    elif process == "*":
        result = multiplyFun(s1, s2)
    elif process == "-":
        result = minusFun(s1, s2)
    else:
        print("Invalid operation. Please choose +, -, *, /.")
        ansver = False
        continue

    # Print the result
    if result is not None:
        print("Result:", result)

    result_check = input("Do you want to perform another operation? Answer y or n: ")

    if result_check.lower() == "n":
        ansver = False
    elif result_check.lower() != "y":
        print("Please enter y or n")

    raund = 2
