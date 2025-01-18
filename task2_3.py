import math

def lcm_gcd(a, b):
    gcd = math.gcd(a, b)
    lcm = (a * b) // gcd
    return lcm, gcd

# Example usage
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
lcm, gcd = lcm_gcd(num1, num2)
print("LCM:", lcm)
print("GCD:", gcd)