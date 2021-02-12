"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, add_mult, add_cubes)


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
        quit()
    elif len(tokens) < 2:
        print("Not enough inputs.")
        continue
   
    operator = tokens[0]
    num1 = float(tokens[1])

    if len(tokens) < 3:
        num2 = 0
    else:
        num2 = float(tokens[2])

    if len(tokens) > 3:
        num3 = float(tokens[3])

    if operator == "+":
        result = add(num1, num2)

    elif operator == "-":
        result = subtract(num1, num2)

    elif operator == "*":
        result = multiply(num1, num2)
        
    elif operator == "/":
        result = divide(num1, num2)

    elif operator == "square":
        result = square(num1)

    elif operator == "cube":
        result = cube(num1)

    elif operator == "pow":
        result = power(num1, num2)

    elif operator == "mod":
        result = mod(num1, num2)

    elif operator == "x+":
        result = add_mult(num1, num2, num3)

    elif operator == "cubes+":
        result = add_cubes(num1, num2)

    print(result)