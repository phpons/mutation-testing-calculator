def is_number(a):
    return isinstance(a, (int, float))

def validate_input(a, b):
    if not is_number(a) or not is_number(b):
        raise ValueError("Input values must be numbers.")

def sum(a, b):
    validate_input(a, b)
    return a + b

def subtract(a, b):
    validate_input(a, b)
    return a - b 

def mult(a, b):
    validate_input(a, b)
    return a * b

def div(a, b):
    validate_input(a, b)
    if b == 0:
        raise ValueError("Can\'t divide by zero.")
    return a/b 