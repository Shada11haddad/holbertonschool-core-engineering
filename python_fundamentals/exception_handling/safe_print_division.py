#!/usr/bin/env python3
def safe_print_division(a, b):
    """Divides 2 integers and prints the result safely.

    Args:
        a: First integer (numerator).
        b: Second integer (denominator).

    Returns:
        The result of the division, or None if division fails.
    """
    result = None
    try:
        result = a / b
    except (ZeroDivisionError, TypeError):
        pass
    finally:
        print("Inside result: {}".format(result))
    return result
