def find_subarray_with_sum(arr, target_sum):
    current_sum = 0
    start_index = 0
    for end_index in range(len(arr)):
        current_sum += arr[end_index]
        while current_sum > target_sum and start_index <= end_index:
            current_sum -= arr[start_index]
            start_index += 1
        if current_sum == target_sum:
            return (start_index, end_index)
    return -1

# Example usage
if __name__ == "__main__":
    print("Subarray indices:", find_subarray_with_sum([1, 2, 3, 7, 5], 12))