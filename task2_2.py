def sum_of_digits(n):
    return sum(map(int, str(n)))

# Example usage
number = int(input("Enter a number: "))
print("Sum of digits:", sum_of_digits(number))