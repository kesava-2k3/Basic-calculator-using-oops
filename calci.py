class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Cannot divide by zero"
        return x / y


def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    calculator = Calculator()

    while True:
        print("\nOptions:")
        print("Enter 'add' for addition")
        print("Enter 'subtract' for subtraction")
        print("Enter 'multiply' for multiplication")
        print("Enter 'divide' for division")
        print("Enter 'quit' to end the program")

        user_input = input(": ").lower()

        if user_input == "quit":
            break
        elif user_input in ("add", "subtract", "multiply", "divide"):
            num1 = get_float_input("Enter the first number: ")
            num2 = get_float_input("Enter the second number: ")

            if user_input == "add":
                print(f"Result: {num1} + {num2} = {calculator.add(num1, num2)}")
            elif user_input == "subtract":
                print(f"Result: {num1} - {num2} = {calculator.subtract(num1, num2)}")
            elif user_input == "multiply":
                print(f"Result: {num1} * {num2} = {calculator.multiply(num1, num2)}")
            elif user_input == "divide":
                result = calculator.divide(num1, num2)
                if isinstance(result, str):
                    print(result)
                else:
                    print(f"Result: {num1} / {num2} = {result}")
        else:
            print("Invalid input. Please enter a valid operation.")


if __name__ == "__main__":
    main()
