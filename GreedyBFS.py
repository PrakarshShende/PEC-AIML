import heapq

graph = {
    'S': ['A', 'B', 'C'],
    'A': ['D'],
    'B': ['D', 'H'],
    'C': ['L'],
    'D': ['F'],
    'H': ['G'],
    'G': ['E'],
    'E': []
}

h = {
    'S': 10,
    'A': 9,
    'B': 7,
    'C': 8,
    'D': 8,
    'H': 6,
    'G': 3,
    'E': 0,
    'F': 6,
    'L': 6
}

def best_first_search(graph, start, goal):
    visited = set()
    queue = [(h[start], start)]

    while queue:
        _, node = heapq.heappop(queue)

        if node in visited:
            continue

        print(node, end=" ")
        visited.add(node)

        if node == goal:
            break

        for neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(queue, (h[neighbor], neighbor))

print("Best First Search:")
best_first_search(graph, 'S', 'E')
