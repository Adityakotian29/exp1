# Constants for the players
MAXIMIZER = 'Max'
MINIMIZER = 'Min'

# Sample game tree
def evaluate(node):
    """Evaluates the leaf nodes of the game tree."""
    return node

def get_children(node):
    """Generates the children of the current node."""
    return [node - 1, node - 2]  # Each player can choose to subtract either 1 or 2

def is_terminal(node):
    """Checks if the node is a terminal node (less than or equal to 0)."""
    return node <= 0

def minimax(node, depth, alpha, beta, maximizing_player):
    if is_terminal(node):
        return evaluate(node)

    if maximizing_player:
        max_eval = float('-inf')
        for child in get_children(node):
            eval = minimax(child, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Beta cut-off
        return max_eval
    else:
        min_eval = float('inf')
        for child in get_children(node):
            eval = minimax(child, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Alpha cut-off
        return min_eval

# Example usage
if __name__ == "__main__":
    starting_node = 5  # Starting point of the game
    best_value = minimax(starting_node, 3, float('-inf'), float('inf'), True)
    print("Best value for Maximizer:", best_value)
