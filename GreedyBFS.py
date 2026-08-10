import heapq

# Graph: node -> connected nodes
graph = {
    'S': ['A', 'B', 'C'],
    'A': ['B', 'D'],
    'B': ['D', 'H'],
    'C': ['L'],
    'D': ['F'],
    'H': ['F', 'G'],
    'L': ['I', 'J'],
    'I': ['K'],
    'J': ['K'],
    'G': ['E'],
    'K': ['E'],
    'F': [],
    'E': []
}

# Heuristic values h(n)
heuristic = {
    'S': 10,
    'A': 9,
    'B': 7,
    'C': 8,
    'D': 8,
    'H': 6,
    'L': 6,
    'F': 6,
    'G': 3,
    'I': 4,
    'J': 4,
    'K': 3,
    'E': 0
}


def best_first_search(start, goal):
    # Priority queue: (heuristic, node)
    open_list = [(heuristic[start], start)]

    closed = []
    parent = {start: None}
    visited = set()

    while open_list:

        # Select node with lowest heuristic
        h, current = heapq.heappop(open_list)

        if current in visited:
            continue

        visited.add(current)
        closed.append(current)

        # Check goal
        if current == goal:
            break

        # Expand current node
        for neighbor in graph[current]:

            if neighbor not in visited:
                if neighbor not in parent:
                    parent[neighbor] = current

                heapq.heappush(
                    open_list,
                    (heuristic[neighbor], neighbor)
                )

        # Display OPEN and CLOSED
        open_nodes = sorted(
            [(h, n) for h, n in open_list if n not in visited]
        )

        print("Open =", [f"{node}{h}" for h, node in open_nodes])
        print("Closed =", [f"{node}{heuristic[node]}" for node in closed])
        print()

    # Construct solution path
    if goal in parent:
        path = []
        current = goal

        while current is not None:
            path.append(current)
            current = parent[current]

        path.reverse()

        print("Solution Path:")
        print(" -> ".join(
            f"{node}{heuristic[node]}" for node in path
        ))
    else:
        print("Goal not found!")


# Execute
best_first_search('S', 'E')
