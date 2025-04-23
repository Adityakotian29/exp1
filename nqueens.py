# def safe(lmao, row, col):
#     num_rows = len(lmao)
#     num_cols = len(lmao[0])
#     if 1 in lmao[row]:
#         return False
#     if any(lmao[i][col] == 1 for i in range(num_rows)):
#         return False
#     for i, j in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
#         r, c = row + i, col + j
#         while 0 <= r < num_rows and 0 <= c < num_cols:
#             if lmao[r][c] == 1:
#                 return False
#             r += i
#             c += j
#     return True

# def place_queens(lmao, i=0, solutions=None):
#     if solutions is None:
#         solutions = []
#     num_rows = len(lmao)
#     if i >= num_rows:
#         solutions.append([row[:] for row in lmao])
#         return
#     for j in range(len(lmao[i])):
#         if safe(lmao, i, j):
#             lmao[i][j] = 1
#             place_queens(lmao, i + 1, solutions)
#             lmao[i][j] = 0
#     return solutions

# def print_solutions(solutions):
#     for i in solutions:
#         for j in i:
#             print(j)
#         print()

# size = int(input("Enter the size of the chessboard: "))
# lmao = [[0] * size for _ in range(size)]
# solution = place_queens(lmao)
# print_solutions(solution)





def safe(lmao, row, col):
    num_rows = len(lmao)
    num_cols = len(lmao[0])

    # Check for any queen in the current row
    if 1 in lmao[row]:
        return False

    # Check for any queen in the current column
    if any(lmao[i][col] == 1 for i in range(num_rows)):
        return False

    # Check diagonals
    for i, j in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        r, c = row + i, col + j
        while 0 <= r < num_rows and 0 <= c < num_cols:
            if lmao[r][c] == 1:
                return False
            r += i
            c += j

    return True

def place_queens(lmao, i=0):
    if i >= len(lmao):
        return True 
    for j in range(len(lmao[i])):
        if safe(lmao, i, j):
            lmao[i][j] = 1  
            if place_queens(lmao, i + 1):  
                return True
            lmao[i][j] = 0 
    return False

# Main Code
size = int(input("matrix ka size bata: "))
lmao = [[0] * size for _ in range(size)]

if place_queens(lmao):
    print("Queens placed successfully:")
    for row in lmao:
        print(row)
else:
    print("No solution exists.")
