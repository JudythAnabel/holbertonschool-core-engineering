#!/usr/bin/env python3
def best_score(a_dictionary):
    """Return the key with the biggest integer value, or None."""
    if not a_dictionary:
        return None
    best = None
    for name in a_dictionary:
        if best is None or a_dictionary[name] > a_dictionary[best]:
            best = name
    return best
