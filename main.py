board = [
    [0, 0, 0, 0, 8, 0, 6, 0, 4],
    [0, 6, 0, 0, 0, 0, 5, 7, 0],
    [0, 4, 0, 7, 0, 0, 0, 0, 0],
    [0, 0, 2, 8, 0, 1, 0, 0, 0],
    [0, 0, 7, 0, 4, 0, 9, 0, 0],
    [0, 0, 0, 5, 0, 3, 1, 0, 0],
    [0, 0, 0, 0, 0, 6, 0, 1, 0],
    [0, 5, 6, 0, 0, 0, 0, 8, 0],
    [2, 0, 4, 0, 5, 0, 0, 0, 0],
]


def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find
    
    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False


def valid(board, number, pos):
    # check row
    for i in range(len(board)):
        if board[pos[0]][i] == number and i != pos[1]:
            return False
    
    #check column
    for i in range(len(board)):
        if board[i][pos[1]] == number and i != pos[0]:
            return False

    #check box
    box_x = pos[1] // 3 
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == number and (i, j) != pos:
                return False
    
    return True



def print_board(board):
    l = 1
    for i in range(0, len(board)):
        k = 1
        for number in board[i]:
            if k % 3 == 0 and k != len(board):
                print(number, end=" | ")
            else:
                print(number, end=" ")
            k += 1
        if l % 3 == 0 and l != len(board):
            print()
            print("------|-------|------")
        else:
            print()
        l += 1


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return (i, j) # row, col
    return None



print_board(board)
print()
print("------SOLVED--------")
print()
solve(board)
print_board(board)