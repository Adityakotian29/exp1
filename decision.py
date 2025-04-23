class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

def minimax(node, depth, maximizing_player):
    if depth == 0 or (node.left is None and node.right is None):
        return node.value
    
    if maximizing_player:
        return max(minimax(node.left, depth - 1, False), minimax(node.right, depth - 1, False))
    else:
        return min(minimax(node.left, depth - 1, True), minimax(node.right, depth - 1, True))

if __name__ == "__main__":
    root = Node()
    root.left = Node(1)
    root.right = Node(5)
    root.left.left = Node(2)
    root.left.right = Node(3)
    root.right.left = Node(1)
    root.right.right = Node(6)

    # Evaluate the Minimax algorithm
    optimal_value = minimax(root, depth=2, maximizing_player=True)
    print("Optimal Value from Minimax:", optimal_value)
