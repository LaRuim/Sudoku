board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
dimension = len(board[0])
factor = int(dimension**0.5)

def solve(Board):
    find = find_empty(Board) #Base case for recursion
    if not find:
        return True
    else:
        row, column = find

    for i in range(1,10):
        if valid(Board, i, (row, column)):
            Board[row][column] = i

            if solve(Board):
                return True

            Board[row][column] = 0

    return False


def valid(Board, num, rowAndcol):
    # Check Row
    for i in range(dimension):
        if Board[rowAndcol[0]][i] == num and rowAndcol[1] != i:
            return False

    # Check Column
    for i in range(dimension):
        if Board[i][rowAndcol[1]] == num and rowAndcol[0] != i:
            return False

    # Check each Box
    box_x = rowAndcol[1] // factor
    box_y = rowAndcol[0] // factor

    for i in range(box_y*factor, box_y*factor + factor):
        for j in range(box_x*factor, box_x*factor + factor):
            if Board[i][j] == num and (i,j) != rowAndcol:
                return False

    return True

def print_board(Board):

    for i in range(len(Board)):
        if i % factor == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(dimension):
            if j%3 == 0 and j!= 0:
                print(" | ",end="")

            if j == 8:
                print(Board[i][j])
            else:
                print(str(Board[i][j]) + " ",end="")


def find_empty(Board):
    for i in range(len(Board)):
        for j in range(dimension):
            if Board[i][j] == 0:
                return (i , j) # row,column(row first,then column)

    return None 

print_board(board)
solve(board)
print("$$$$$$$$$$$$$$$$$$$$$$$$") 
print_board(board)                    