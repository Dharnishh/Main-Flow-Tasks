def sort_list(lst):
    return sorted(lst)

user_input = input("Enter a list of integers (separated by spaces): ")
# Example usage with pre-defined list
original_list = [int(x) for x in user_input.split()]  
sorted_list = sort_list(original_list)
print("Original list:", original_list)
print("Sorted list:", sorted_list)