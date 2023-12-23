

def is_safe(x, y, board):
    """Check if x and y are valid indexes for N*N chessboard"""
    return (0 <= x < 8) and (0 <= y < 8) and (board[x][y] == -1)

def print_solution(n, board):
    """Function to print chessboard matrix"""
    for i in range(n):
        for j in range(n):
            print(f'{board[i][j]:02}', end=' ')
        print()

def solve_kt_util(n, board, curr_x, curr_y, move_x, move_y, pos):
    """Utility function to solve Knight Tour problem using Backtracking"""
    if pos == n**2:
        return True

    # Try all next moves from the current coordinate x, y
    for i in range(8):
        next_x = curr_x + move_x[i]
        next_y = curr_y + move_y[i]
        if is_safe(next_x, next_y, board):
            board[next_x][next_y] = pos
            if solve_kt_util(n, board, next_x, next_y, move_x, move_y, pos+1):
                return True
            # Backtracking
            board[next_x][next_y] = -1
    return False

def solve_kt():
    """This function solves the Knight Tour problem using Backtracking. 
    It returns false if no complete tour is possible, otherwise return true and prints the tour."""
    n = 8
    board = [[-1 for i in range(n)] for j in range(n)]

    # xMove[] and yMove[] define next move of Knight.
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    # Since the Knight is initially at the first block
    board[0][0] = 0

    # Step counter for knight's position
    pos = 1

    # Check if solution exists or not
    if not solve_kt_util(n, board, 0, 0, move_x, move_y, pos):
        print("Solution does not exist")
        return False
    else:
        print_solution(n, board)
        return True

# Calling function
solve_kt()
