# nqueen
def check(row, col):    # 대각선에 위치하면 안 됨
    for i in range(row):
        if abs(i - row) == abs(board[i] - col):
            return False
    return True

def nqueen(row):
    global cnt
    # 기저 조건
    if row == n:
        cnt += 1
        return
    else:
        for col in range(n):
            if not visited[col] and check(row, col):
                board[row] = col    # row, col 위치에 퀸 배치
                visited[col] = True
                nqueen(row + 1)
                visited[col] = False


n = int(input())
board = [-1] * n
visited = [False for _ in range(n)]  # 가로 확인
cnt = 0
nqueen(0)
print(cnt)