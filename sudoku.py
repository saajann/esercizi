def stampa(board):
    for i in board:
        t = ''
        for j in i:
            t += f'{j} '
        print(t)
def vuote(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return [i,j]
    return None
def check(board,i,j,n):
    #CTRL colonna
    for x in range(9):
        if n == board[x][j]:
            return False
    #CTRL riga
    if n in board[i]:
        return False
    #CTRL 3x3
    start_i, start_j = 3*(i//3), 3*(j//3)
    for x in range(3):
        for y in range(3):
            if board[start_i + x][start_j + y] == n:
                return False
    #Se valido
    return True
def risolvi(board):
    xy = vuote(board)   
    if not xy:
        return True 
    i,j = xy           
    for n in range(1,10):
        if check(board,i,j,n):
            board[i][j] = n
            if risolvi(board):
                return True
            board[i][j] = 0
    return False
sudoku = [[3,7,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,8,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,4,0,0,0],
          [0,0,0,1,0,0,0,0,0],
          [0,0,0,0,5,0,0,0,0],
          [0,0,0,0,0,0,0,0,0]]
if risolvi(sudoku):
    stampa(sudoku)
else: 
    print('Sudoku non risolvibile')