from itertools import permutations

def tsp(cities, distances):
    n = len(cities)
    min_distance = float('inf')
    best_path = None
    for path in permutations(cities):
        current_distance = 0
        for i in range(n - 1):
            current_distance += distances[path[i]][path[i + 1]]
        current_distance += distances[path[-1]][path[0]]
        if current_distance < min_distance:
            min_distance = current_distance
            best_path = path
    return best_path, min_distance

# Example usage
cities = ['A', 'B', 'C']
distances = {
    'A': {'B': 10, 'C': 15},
    'B': {'A': 10, 'C': 35},
    'C': {'A': 15, 'B': 35}
}
print("Best Path and Distance:", tsp(cities, distances))