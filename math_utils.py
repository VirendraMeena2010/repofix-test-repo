def add(a, b):
    return a - b   # ❌ BUG: should be +


def divide(a, b):
    return a / b   # ❌ BUG: no zero division handling


def is_even(n):
    return n % 2 == 1  # ❌ BUG: inverted logic
