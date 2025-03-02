def merge_intervals(intervals):
    if not intervals:
        return []
    intervals.sort()
    merged = [intervals[0]]
    for current in intervals[1:]:
        if current[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], current[1])
        else:
            merged.append(current)
    return merged

# Example usage
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print("Merged Intervals:", merge_intervals(intervals))