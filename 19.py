def is_substring(s1, s2):
    return s2 in s1

s1 = input("Enter the main string: ")
s2 = input("Enter the substring: ")
result = is_substring(s1, s2)
print(f"Is '{s2}' a substring of '{s1}'? {result}")
