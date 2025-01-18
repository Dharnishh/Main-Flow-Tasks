def reverse_list(lst):
    return lst[::-1]

# Get input from the user
user_input = input("Enter a list of integers (separated by spaces): ")
# Convert the input string to a list of integers
original_list = [int(x) for x in user_input.split()]

reversed_list = reverse_list(original_list)
print("Original list:", original_list)
print("Reversed list:", reversed_list)