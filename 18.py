def swap_numbers(a, b):
    a, b = b, a
    return a, b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a, b = swap_numbers(a, b)
print(f"Swapped values: a = {a}, b = {b}")
