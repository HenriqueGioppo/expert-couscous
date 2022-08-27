def get_input_numOne():
    num_one = input("Input the first number: ")
    if num_one.isdigit():
        number_one = (int(num_one))
        get_input_operation(number_one, num_one)
        return number_one
    else:
        print("\nGib me a numba")
        get_input_numOne()


def get_input_operation(number_one, num_one):
    operation = input("Input the operation you want to execute: ")
    if operation == '+' or operation == '-' or operation == '*' or operation == '/':
        get_input_numTwo(number_one, num_one, operation)
        return operation
    else:
        print("\nthis is not a valid operation")
        get_input_operation(number_one, num_one)


def get_input_numTwo(number_one, num_one, operation):
    num_two = input("Input the second number: ")
    if num_two.isdigit():
        number_two = (int(num_two))
        exec_calc(number_one, num_one, number_two, num_two, operation)
        return number_two
    else:
        print("\nGib me a numba")
        get_input_numTwo()


def exec_calc(number_one, num_one, number_two, num_two, operation):
    result = 0
    if operation == "+":
        result = number_one + number_two
        print_result(num_one, num_two, operation, result)
    elif operation == "-":
        result = number_one - number_two
        print_result(num_one, num_two, operation, result)
    elif operation == "*":
        result = number_one * number_two
        print_result(num_one, num_two, operation, result)
    elif operation == "/":
        result = number_one / number_two
        print_result(num_one, num_two, operation, result)
    return result


def print_result(num_one, num_two, operation, result):
    res = (str(result))
    print("\nYour equation was: " + num_one + operation + num_two +
          " and the result is: " + res)
    continue_exec()


def continue_exec():
    continue_calc = input("\nDo you want to continue 'Y'/'N': ")
    continue_calc = continue_calc.upper()
    if continue_calc == 'Y':
        get_input_numOne()
    elif continue_calc == 'N':
        print("\nGood bye!")
        exit()
    else:
        print("\nOnly choose between Y or N")
        continue_exec()


get_input_numOne()