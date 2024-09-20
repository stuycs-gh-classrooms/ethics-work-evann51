board = [[0]*3]*3
def createBoard():
    for i in range(len(board)):
        for n in range(len(board[i])):
            board[i][n] = "☐"

def drawTTT():
    for b in range(len(board)):
        print(board[b][0]+"|"+board[b][1]+"|"+board[b][2])
        if(b == 1) or (b == 0):
            print('-----')
createBoard()
drawTTT()
