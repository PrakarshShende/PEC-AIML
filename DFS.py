def dfs(graph, start, goal):

    OPEN = [start]
    CLOSED = []
    traversal = []

    while OPEN:

        x = OPEN.pop(0)

        # Add node to traversal
        traversal.append(x)

        # Check if goal is reached
        if x == goal:
            print("DFS Traversal:", " → ".join(traversal))
            print("Goal found:", x)
            return

        # Add current node to CLOSED
        if x not in CLOSED:
            CLOSED.append(x)

            # Get children
            children = graph[x]

            # Add children to LEFT of OPEN
            for child in reversed(children):

                if child not in OPEN and child not in CLOSED:
                    OPEN.insert(0, child)

    print("Goal not found")


# Tree
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': [],
    'D': [],
    'E': []
}

# DFS
dfs(graph, 'A', 'E')
