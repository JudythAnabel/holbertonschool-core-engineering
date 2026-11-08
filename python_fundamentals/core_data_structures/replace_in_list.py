#!/usr/bin/env python3
def replace_in_list(my_list, idx, element):
    """Replace the element at idx with element and return the list."""
    if 0 <= idx < len(my_list):
        my_list[idx] = element
    return my_list
