# Here's the full code that will attempt to find a closed tour first, and if not found, will find an open tour.

def is_safe(x, y, board):
    """Check if x and y are valid indexes for N*N chessboard"""
    return 0 <= x < 8 and 0 <= y < 8 and board[x][y] == -1

def print_solution(n, board):
    """Function to print chessboard matrix"""
    for i in range(n):
        for j in range(n):
            print(f'{board[i][j]:02}', end=' ')
        print()
    print()

def warnsdorffs_heuristics(board, move_x, move_y, x, y):
    """Warnsdorff's heuristic to prioritize next moves with fewer onward moves."""
    moves = []
    for i in range(8):
        next_x, next_y = x + move_x[i], y + move_y[i]
        if is_safe(next_x, next_y, board):
            count = 0
            for j in range(8):
                if is_safe(next_x + move_x[j], next_y + move_y[j], board):
                    count += 1
            moves.append((count, i))
    moves.sort()
    return [move[1] for move in moves]

def solve_kt_util(n, board, curr_x, curr_y, move_x, move_y, pos, closed_tour=False):
    """Utility function to solve Knight Tour problem using Backtracking and Warnsdorff's heuristic"""
    if pos == n**2:
        if closed_tour:
            # Check if the last position attacks the start (closed tour)
            for i in range(8):
                if curr_x + move_x[i] == 0 and curr_y + move_y[i] == 0:
                    return True
            return False
        else:
            # For open tour, no need to return to start
            return True

    sorted_moves = warnsdorffs_heuristics(board, move_x, move_y, curr_x, curr_y)
    for i in sorted_moves:
        next_x = curr_x + move_x[i]
        next_y = curr_y + move_y[i]
        if is_safe(next_x, next_y, board):
            board[next_x][next_y] = pos
            if solve_kt_util(n, board, next_x, next_y, move_x, move_y, pos+1, closed_tour):
                return True
            board[next_x][next_y] = -1  # Backtracking
    return False

def solve_kt(n, closed_tour=False):
    """This function solves the Knight Tour problem using Backtracking and Warnsdorff's heuristic."""
    board = [[-1 for i in range(n)] for j in range(n)]
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]
    board[0][0] = 0

    if not solve_kt_util(n, board, 0, 0, move_x, move_y, 1, closed_tour):
        if closed_tour:
            print("No closed tour found. Trying to find an open tour...")
            return solve_kt(n, closed_tour=False)
        else:
            print("No open tour found.")
            return False
    else:
        print_solution(n, board)
        return True

# Attempt to find a closed tour first, if not found, find an open tour
solve_kt(8, closed_tour=True)
