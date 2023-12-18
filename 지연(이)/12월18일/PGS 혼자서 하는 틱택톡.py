# 1. 3*3 전체 탐색, 모든 경우의 수를 대비 해도 될듯. 1이 되는 경우
# 2. O count X count, O line count, X line count 이걸로 비교 해서 파악할 수도 있을듯

def solution(board):
    O, X, O_line, X_line = 0,0,0,0
    for i in range(3):
        # 가로
        if board[i][0]==board[i][1]==board[i][2]=='O':
            O_line+=1
        elif board[i][0]==board[i][1]==board[i][2]=='X':
            X_line+=1

        # 세로
        if board[0][i] == board[1][i] == board[2][i] == 'O':
            O_line+=1
        elif board[0][i] == board[1][i] == board[2][i] == 'X':
            X_line+=1

        # 대각선
        if board[0][0]==board[1][1]==board[2][2]=='O':
            O_line+=1
        elif board[0][0]==board[1][1]==board[2][2]=='X':
            X_line+=1

        O += board[i].count('O')
        X += board[i].count('X')

    print(O,X, O_line, X_line)
    #
    if X==O:
        if O_line:
            return 0
        if X>4:
            return 0

        if X_line:
            if (X==3 or X==4) and X_line==1:
                return 1
            else:
                return 0
        else:
            return 1

    elif O==X+1:
        if X_line:
            return 0
        if O>5:
            return 0

        if O_line==0:
            return 1
        else:
            if (O_line==1 or (O_line==2 and O==5)):
                return 1
            else:
                return 0
    else:
        return 0

print(solution(["O.X", ".O.", "..X"])) # 1
print(solution(["OOO", "...", "XXX"])) # 0
print(solution(["...", ".X.", "..."])) # 0
print(solution(["...", "...", "..."])) # 1
print(solution(["OXX", "OOX", "OXO"])) # 1
