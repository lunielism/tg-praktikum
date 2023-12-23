def is_safe(x, y, board):
    return 0 <= x < 8 and 0 <= y < 8 and board[x][y] == -1

def print_solution(n, board):
    for i in range(n):
        for j in range(n):
            print(f'{board[i][j]:02}', end=' ')
        print()
    print()

def warnsdorffs_heuristics(board, move_x, move_y, x, y):
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
    if pos == n**2:
        if closed_tour:
            for i in range(8):
                if curr_x + move_x[i] == 0 and curr_y + move_y[i] == 0:
                    return True
            return False
        else:
            return True

    sorted_moves = warnsdorffs_heuristics(board, move_x, move_y, curr_x, curr_y)
    for i in sorted_moves:
        next_x = curr_x + move_x[i]
        next_y = curr_y + move_y[i]
        if is_safe(next_x, next_y, board):
            board[next_x][next_y] = pos
            if solve_kt_util(n, board, next_x, next_y, move_x, move_y, pos+1, closed_tour):
                return True
            board[next_x][next_y] = -1
    return False

def solve_kt(n, start_x, start_y, closed_tour=False):
    board = [[-1 for _ in range(n)] for _ in range(n)]
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]
    board[start_x][start_y] = 0

    if not solve_kt_util(n, board, start_x, start_y, move_x, move_y, 1, closed_tour):
        print("No solution found for this type of tour.")
    else:
        print_solution(n, board)

# Attempt to find both a closed and an open Knight's Tour
print("Attempting to find a closed Knight's Tour:")
solve_kt(8, 0, 0, True)

print("Attempting to find an open Knight's Tour:")
solve_kt(8, 0, 0, False)
