"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# repeat forever:
    # read input
    # tokenize input
    # if the first token is "q":
        # quit

    # else:
        # decide which math function to call based on first token
    # If first token is pow, call power function with other 2 tokens

while True:
    input_str = input("> ")
    tokens = input_str.split(' ')
  
    if tokens[0] == "q":
        quit
    else:
        operator = tokens[0]
        num1 = float(tokens[1])
        num2 = float(tokens[2])

        if operator == "+":
            print(add(num1, num2))
        elif operator == "-":
            print(subtract(num1, num2))
        elif operator == "*":
            multiply(num1, num2)
        elif operator == "/":
            divide(num1, num2)
        elif operator == "pow":
            power(num1, num2)
        