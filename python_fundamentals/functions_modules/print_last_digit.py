#!/usr/bin/env python3
def print_last_digit(number):
    """Print the last digit of number and return it."""
    digit = abs(number) % 10
    print("{}".format(digit), end="")
    return digit
