def find_second_largest(lst):
    if len(lst) < 2:
        return None
    first, second = float('-inf'), float('-inf')
    for number in lst:
        if number > first:
            first, second = number, first
        elif number > second and number != first:
            second = number
    return second

numbers = [10, 20, 4, 45, 99]
second_largest = find_second_largest(numbers)
print(f"The second largest number is {second_largest}")
