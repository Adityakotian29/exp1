class Node:
    def __init__(self, name, heuristic):
        self.name = name
        self.heuristic = heuristic
        self.children = []
        self.parent = None

def bfs(start, goal):
    open_list = [start]
    while open_list:
        # Sort nodes by heuristic value, lowest first (greedy best-first search)
        open_list.sort(key=lambda node: node.heuristic)
        current = open_list.pop(0)

        # Check if the goal node is reached
        if current.name == goal.name:
            return current

        # Add each child of the current node to the open list
        for child in current.children:
            child.parent = current
            open_list.append(child)

def print_path(node):
    path = []
    while node:
        path.append(node.name)
        node = node.parent
    return path[::-1]  # Reverse the path to show from start to goal

# Initialize nodes with names and heuristic values
start = Node("start", 6)
goal = Node("goal", 0)
a = Node("a", 3)
b = Node("b", 5)
c = Node("c", 4)
d = Node("d", 2)
e = Node("e", 1)
f = Node("f", 3)
g = Node("g", 1)

# Define the connections between nodes
start.children = [a, b, c]
a.children = [d, e]
b.children = [f]
c.children = [g]
e.children = [goal]

# Perform search and print the results
result = bfs(start, goal)
if result:
    path = print_path(result)
    print("Found:", result.name)
    print("Path traveled:", " -> ".join(path))
else:
    print("Goal not found.")
