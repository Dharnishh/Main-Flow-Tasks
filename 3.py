def find_duplicates(lst):
    from collections import Counter
    counts = Counter(lst)
    return [item for item, count in counts.items() if count > 1]

# Example usage
lst = [1, 2, 2, 3, 4, 4, 5]
print(find_duplicates(lst))
