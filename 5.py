import heapq

def k_largest_elements(lst, k):
    return heapq.nlargest(k, lst)

# Example usage
lst = [3, 2, 1, 5, 6, 4]
k = 2
print(k_largest_elements(lst, k))
