def has_cycle(graph):
    def dfs(node, visited, rec_stack):
        visited[node] = True
        rec_stack[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                if dfs(neighbor, visited, rec_stack):
                    return True
            elif rec_stack[neighbor]:
                return True
        rec_stack[node] = False
        return False

    visited = {node: False for node in graph}
    rec_stack = {node: False for node in graph}
    for node in graph:
        if not visited[node]:
            if dfs(node, visited, rec_stack):
                return True
    return False

# Example usage
graph = {
    'A': ['B'],
    'B': ['C'],
    'C': ['A']
}
print("Graph Contains Cycle:", has_cycle(graph))