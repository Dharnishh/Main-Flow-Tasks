def string_length(s):
    count = 0
    for _ in s:
        count += 1
    return count

# Example usage with pre-defined string
text = input("enter a string:")
length = string_length(text)
print("Length of the string:", length)