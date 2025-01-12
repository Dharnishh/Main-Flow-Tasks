def is_armstrong_number(n):
    num_str = str(n)
    num_len = len(num_str)
    sum_of_powers = sum(int(digit) ** num_len for digit in num_str)
    return sum_of_powers == n

number = int(input("Enter an integer: "))
result = is_armstrong_number(number)
print("Is the number an Armstrong number?", result)