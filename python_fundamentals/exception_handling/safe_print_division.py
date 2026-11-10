#!/usr/bin/env python3
def safe_print_division(a, b):
    """Divide a by b, print the result, and return it (or None)."""
    try:
        result = a / b
    except (ZeroDivisionError, TypeError):
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
