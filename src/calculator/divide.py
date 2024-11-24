def divide(a, b):
    #"""Returns the division of a by b. Raises an exception if b is 0."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b