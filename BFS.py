def bfs(graph, start, goal):

    OPEN = [start]
    CLOSED = []
    traversal = []

    while OPEN:

        # Remove the leftmost node from OPEN
        x = OPEN.pop(0)

        # Add node to traversal
        traversal.append(x)

        # Check if goal is reached
        if x == goal:
            print("BFS Traversal:", " → ".join(traversal))
            print("Goal found:", x)
            return

        # Add current node to CLOSED
        if x not in CLOSED:
            CLOSED.append(x)

            # Get children of current node
            children = graph[x]

            # Add children to RIGHT of OPEN
            for child in children:

                if child not in OPEN and child not in CLOSED:
                    OPEN.append(child)

    print("Goal not found")


# Tree
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': [],
    'D': [],
    'E': []
}

# Call BFS
bfs(graph, 'A', 'E')
