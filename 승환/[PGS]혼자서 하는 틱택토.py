def solution(board):
    answer = 1
    # 중단해야 하는 경우 : 3개가 완성되었을 때
    # X가 O보다 더 많은 경우
    # O가 X보다 2개 이상 많은 경우
    cnto = 0  # o 갯수
    cntx = 0  # x 갯수
    cntt = 0  # 전체 갯수
    # 끝났을 때 o, x 체크 o = 0, x = 1
    chkf = -1
    for i in range(3):
        for j in range(3):
            # 대각선 확인
            if i == 0 and j == 0 and board[i][j] != '.':
                if board[i][j] == board[1][1] == board[2][2]:
                    # O로 끝났는데 X로 끝나는 경우..
                    if chkf == 0 and board[i][j] == 'X':
                        return 0
                    # X로 끝났는데 O로 끝나는 경우
                    if chkf == 1:
                        return 0
                    # O로 끝나는 경우
                    if board[i][j] == 'O':
                        chkf = 0
                    # X로 끝나는 경우
                    else:
                        chkf = 1
            if i == 2 and j == 0 and board[i][j] != '.':
                if board[i][j] == board[1][1] == board[0][2]:
                    # O로 끝났는데 X로 끝나는 경우..
                    if chkf == 0 and board[i][j] == 'X':
                        return 0
                    # X로 끝났는데 O로 끝나는 경우
                    if chkf == 1:
                        return 0
                    # O로 끝나는 경우
                    if board[i][j] == 'O':
                        chkf = 0
                    # X로 끝나는 경우
                    else:
                        chkf = 1
            if i == 0 and board[i][j] != '.':
                if board[i][j] == board[1][j] == board[2][j]:
                    # O로 끝났는데 X로 끝나는 경우..
                    if chkf == 0 and board[i][j] == 'X':
                        return 0
                    # X로 끝났는데 또 끝나는 케이스
                    if chkf == 1:
                        return 0
                    # O로 끝나는 경우
                    if board[i][j] == 'O':
                        chkf = 0
                    # X로 끝나는 경우
                    else:
                        chkf = 1
            if j == 0 and board[i][j] != '.':
                if board[i][j] == board[i][1] == board[i][2]:
                    # O로 끝났는데 X로 끝나는 경우..
                    if chkf == 0 and board[i][j] == 'X':
                        return 0
                    # X로 끝났는데 또 끝나는 경우
                    if chkf == 1:
                        return 0
                    # O로 끝나는 경우
                    if board[i][j] == 'O':
                        chkf = 0
                    # X로 끝나는 경우
                    else:
                        chkf = 1
            if board[i][j] == 'O':
                cnto += 1
            elif board[i][j] == 'X':
                cntx += 1
    # O로 빙고를 완성한 경우 O가 x개수보다 1개 더 많아야함
    print(chkf, cnto, cntx)
    if chkf == 0:
        if cnto == cntx + 1:
            pass
        else:
            return 0
    # X로 빙고를 완성한 경우 O와 X개수가 같아야 함
    if chkf == 1:
        if cnto == cntx:
            pass
        else:
            return 0
    # O개수가 X보다 2개이상 많은 경우
    if cnto > cntx + 1:
        return 0
    # X개수가 O보다 많은 경우
    if cnto < cntx:
        return 0
            
    return answer
