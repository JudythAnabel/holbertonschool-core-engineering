#!/usr/bin/env python3
def safe_print_integer(value):
    """Print value as an integer and return True, or return False."""
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError):
        return False
    else:
        return True
