def find_missing_number(arr):
    n = len(arr) + 1
    total_sum = n * (n + 1) // 2
    return total_sum - sum(arr)

# Example usage
if __name__ == "__main__":
    print("Missing Number:", find_missing_number([1, 2, 4, 5, 6]))