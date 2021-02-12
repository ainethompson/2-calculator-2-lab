"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

tokens = input_str.split(' ')

# repeat forever:
    # read input
    # tokenize input
    # if the first token is "q":
        # quit

    # else:
        # decide which math function to call based on first token
    # If first token is pow, call power function with other 2 tokens
