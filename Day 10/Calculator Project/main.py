from art import*
print(logo)

def calculation_logic(op,first,next):
    if first < 0:
        return "Involved number"

    if op == "+":
        return first + next
    elif op == "-":
        return first - next
    elif op == "*":
        return first * next
    else:
        return first / next

while True:
    first_num = int(input("what is the first number: "))


    while True:

        print("+\n-\n*\n/")
        operation = input("Pick an operation: ")
        next_num = int(input("what is the next number: "))

        result = calculation_logic(operation,first_num,next_num)
        print(f"{first_num} {operation} {next_num} = {result}")

        choice = input(f"Type 'y' to keep on with {result}, type 'n' to start a new calculation: ").lower()

        if choice == "y":
            first_num = result
        else:
            print("\n" * 20)
            break





