def count_inversions(arr):
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr, 0
        mid = len(arr) // 2
        left, inv_left = merge_sort(arr[:mid])
        right, inv_right = merge_sort(arr[mid:])
        merged, inv_merge = merge(left, right)
        total = inv_left + inv_right + inv_merge
        return merged, total

    def merge(left, right):
        result = []
        i = j = 0
        inv = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                inv += len(left) - i
        result.extend(left[i:])
        result.extend(right[j:])
        return result, inv

    _, total_inversions = merge_sort(arr)
    return total_inversions

# Example usage
arr = [1, 3, 5, 2, 4, 6]
print("Number of Inversions:", count_inversions(arr))