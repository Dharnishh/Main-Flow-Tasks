def remove_duplicates(lst):
    return list(set(lst))

user_input = input("Enter a list of integers (separated by spaces): ")

# Example usage with pre-defined list
original_list = [int(x) for x in user_input.split()]  
unique_list = remove_duplicates(original_list)
print("Original list:", original_list)
print("Unique list:", unique_list)