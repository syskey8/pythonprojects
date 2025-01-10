logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
operation_list = r'''
+
-
*
/
'''
def calculate(first_number, second_number, operation):
    if operation == '+':
        return first_number + second_number
    elif operation == '-':
        return first_number - second_number
    elif operation == '*':
        return first_number * second_number
    elif operation == '/':
        return first_number / second_number
    
def initial_calculation():
    first_number = float(input("What is the first number?: "))
    print(operation_list)
    operation = input("Pick an operation: ")
    second_number = float(input("What is the next number?: "))
    answer = calculate(first_number, second_number, operation)
    print(f"{first_number} {operation} {second_number} = {answer}")
    choice = input(f"Type 'y' to continue calulating with {answer}, or type 'n' to start a new calculation: ")
    if choice == 'y':
        next_calculation(answer)
    elif choice == 'n':
        initial_calculation()
    else:
        print("Wrong input, quitting application")

def next_calculation(answer):
    first_number = float(answer)
    print(operation_list)
    operation = input("Pick an operation: ")
    second_number = float(input("What is the next number?: "))
    answer = calculate(first_number, second_number, operation)
    print(f"{first_number} {operation} {second_number} = {answer}")
    choice = input(f"Type 'y' to continue calulating with {answer}, or type 'n' to start a new calculation: ")
    if choice == 'y':
        next_calculation(answer)
    elif choice == 'n':
        initial_calculation()
    else:
        print("Wrong input, quitting application")

def main():
    print(logo)
    initial_calculation()

main()