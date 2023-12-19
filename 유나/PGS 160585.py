# 성공 요건이 2개 이상인 경우: 한 자리에서 두 번 성공은 한 번으로 친다!
# x의 개수가 O의 개수보다 많은 경우, O의 개수가 X 개수 + 1 보다 많은 경우
# 후공이 성공한 경우에 O가 더 많은 경우, 선공이 성공한 경우에 X가 O와 동일한 경우
# 6(1) 23(1) 30(1) 33(1) : 성공이어야 하는데 0 반환
def solution(board):
    answer = 1
    count_x = count_o = sucess_x = sucess_o = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != '.':
                # 성공 요건을 갖춘 친구인가? 우, 대각선 좌우, 하 체크
                for di, dj in [[0, 1], [1, -1], [1, 1], [1, 0]]:
                    ni, nj  = i + di, j + dj
                    # 범위 내에 존재하고, 다음 칸이 성공인 경우
                    if 0 <= ni < 3 and 0 <= nj < 3 and board[ni][nj] == board[i][j]:
                        # 그 다음 칸도 조건에 맞는지 체크
                        fi, fj  = i + di*2, j + dj*2
                        if 0 <= fi < 3 and 0 <= fj < 3 and board[fi][fj] == board[i][j]:
                            if board[i][j] =='X':
                                sucess_x += 1
                            else:
                                sucess_o += 1
                            break
                # O 개수, X 개수 세기
                if board[i][j] == 'X':
                    count_x += 1
                else:
                    count_o += 1
    
    if (count_x > count_o)  or (count_o > count_x + 1) or (sucess_x and count_x < count_o) or (sucess_o and count_x >= count_o):
        answer = 0
    return answer
