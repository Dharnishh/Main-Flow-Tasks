def decimal_to_binary(n):
    return bin(n)[2:]

n = int(input("Enter a decimal number: "))
binary_representation = decimal_to_binary(n)
print(f"Binary representation of {n} is {binary_representation}")
