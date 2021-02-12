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
  
    if "q" in tokens:
        print("Exiting now.")
        break

    elif len(tokens) < 2:
        print("Not enough inputs.")
        continue

    operator = tokens[0]
    num1 = tokens[1]

    if len(tokens) < 3:
        num2 = "0"
    else:
        num2 = tokens[2]

    if len(tokens) > 3:
        num3 = tokens[3]

    if not num1.isdigit() or not num2.isdigit():
        print("Those aren't numbers!")
        continue

    result = None
    

    if operator == "+":
        result = add(float(num1), float(num2))

    elif operator == "-":
        result = subtract(float(num1), float(num2))

    elif operator == "*":
        result = multiply(float(num1), float(num2))
        
    elif operator == "/":
        result = divide(float(num1), float(num2))

    elif operator == "square":
        result = square(float(num1))

    elif operator == "cube":
        result = cube(float(num1))

    elif operator == "pow":
        result = power(float(num1), float(num2))

    elif operator == "mod":
        result = mod(float(num1), float(num2))

    elif operator == "x+":
        result = add_mult(float(num1), float(num2), float(num3))

    elif operator == "cubes+":
        result = add_cubes(float(num1), float(num2))
    
    else:
        result = "Please enter an operator followed by 2 integers"

    print(result)