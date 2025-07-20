def add(a, b):
    return a + b
def divide(a, b):
    if b == 0:
        raise ValueError("Division par zéro impossible")
    return a / b
def is_even(number):
 return number % 2 == 0