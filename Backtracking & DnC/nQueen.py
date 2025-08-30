def isPossible(n,board,col,row):
    # Firstly Check All The backward Row
    for j in range(col,-1,-1):
        if board[row][j]=='Q':
            return False
        
    # Second Check The Upward Backward Area
    i = row
    j = col
    while i>=0 and j>=0:
        if board[i][j]=='Q':
            return False
        else:
            i-=1
            j-=1

    # Third Check the Foward Lowe Portion
    i = row
    j = col
    while i<n and j>=0:
        if board[i][j]=='Q':
            return False
        else:
            i+=1
            j-=1
    return True


def nQueens(n,board,col):
    if col>=n:
        for i in board:
            print(i)
        print('\n\n')
        print()
        return
    else:
        for i in range(0,n):
            if isPossible(n,board,col,i):
                board[i][col] = 'Q'
                nQueens(n,board,col+1)
                board[i][col] = '-'




n = int(input("Enter the N Queens : "))
board = [['-' for _ in range(n)] for _ in range(n)]
col = 0
# print(board)
nQueens(n,board,col)