# 혼자서 하는 틱택토

def solution(board):
    answer = -1
    
    o_count = 0
    x_count = 0
    
    o_win = False
    x_win = False
        
    def isWin(symbol):
        if board[0][0] == board[0][1] == board[0][2] == symbol:
            return True
        if board[1][0] == board[1][1] == board[1][2] == symbol:
            return True
        if board[2][0] == board[2][1] == board[2][2] == symbol:
            return True
        if board[0][0] == board[1][0] == board[2][0] == symbol:
            return True
        if board[0][1] == board[1][1] == board[2][1] == symbol:
            return True
        if board[0][2] == board[1][2] == board[2][2] == symbol:
            return True
        if board[0][0] == board[1][1] == board[2][2] == symbol:
            return True
        if board[0][2] == board[1][1] == board[2][0] == symbol:
            return True

    
    if isWin('O'):
        o_win = True
    if isWin('X'):
        x_win = True
        
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O':
                o_count += 1
            if board[i][j] == 'X':
                x_count += 1
        
    
    if o_count < x_count:
        answer = 0
    
    elif o_count - x_count >= 2:
        answer = 0
    
    elif o_win and (o_count - x_count != 1):
        answer = 0
    
    elif x_win and (o_count != x_count):
        answer = 0
    
    elif o_win and x_win:
        answer = 0
        
    else:
        answer = 1
        
    return answer