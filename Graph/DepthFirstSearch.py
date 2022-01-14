graph = {
    'A': set(['B', 'C', "D"]),
    'B': set(['E', "F"]),
    'C': set(['G', "I"]),
    'D': set(["I"]),
    'E': set(),
    "F": set(),
    'G': set(),
    "I": set()
}

visited = set()


def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


print("Following is the Depth-First Search")
dfs(visited, graph, 'A')
