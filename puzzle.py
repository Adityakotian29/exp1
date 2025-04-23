class PuzzleNode:
    def __init__(self, state, parent=None, move=None, cost=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.cost = cost

def swap(state, i1, j1, i2, j2):
    state[i1][j1], state[i2][j2] = state[i2][j2], state[i1][j1]

def heuristic(state, target):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != target[i][j]:
                count += 1
    return count

def get_blank_position(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def generate_children(node, target):
    children = []
    i, j = get_blank_position(node.state)
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for move in moves:
        new_i, new_j = i + move[0], j + move[1]
        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_state = [row[:] for row in node.state]
            swap(new_state, i, j, new_i, new_j)
            h = heuristic(new_state, target)
            child = PuzzleNode(new_state, node, move, node.cost + 1 + h)
            children.append(child)
    return children

def solve_puzzle(start, target):
    start_node = PuzzleNode(start)
    target_node = PuzzleNode(target)
    visited = set()
    queue = [start_node]
    
    while queue:
        node = queue.pop(0)
        visited.add(tuple(map(tuple, node.state)))

        if node.state == target_node.state:
            path = []
            while node:
                path.append((node.state, node.move))
                node = node.parent
            path.reverse()
            return path
        
        children = generate_children(node, target)
        for child in children:
            if tuple(map(tuple, child.state)) not in visited:
                queue.append(child)
                visited.add(tuple(map(tuple, child.state)))

    return None


jumbled_matrix = [
    [1, 2, 3],
    [4, 0, 5],
    [6, 7, 8]
]

target_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]


solution = solve_puzzle(jumbled_matrix, target_matrix)


if solution:
    print("Solution steps:")
    for step, (state, move) in enumerate(solution):
        print(f"Step {step + 1}: Move {move} ->")
        for row in state:
            print(row)
        print()
else:
    print("No solution found.")


