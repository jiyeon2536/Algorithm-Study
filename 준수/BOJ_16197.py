from collections import deque


def check_block(x, y):
    if not check_range(x, y):
        return True

    if matrix[x][y] == '#':
        return False
    else:
        return True


def check_range(x, y):
    if 0 <= x < N and 0 <= y < M:
        return True
    else:
        return False


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())

coin1_x, coin1_y = -1, -1
coin2_x, coin2_y = -1, -1

matrix = []

for n in range(N):
    temp = list(input())

    for m in range(M):
        if temp[m] == 'o':
            if coin1_x == coin1_y == -1:
                coin1_x, coin1_y = n, m
            else:
                coin2_x, coin2_y = n, m

    matrix.append(temp)

queue = deque()
queue.append((coin1_x, coin1_y, coin2_x, coin2_y, 0))
answer = -1

while queue:
    x1, y1, x2, y2, cnt = queue.popleft()

    if cnt > 10:
        continue

    check1 = check_range(x1, y1)
    check2 = check_range(x2, y2)

    if check1 and check2:
        for move in range(4):
            nx1 = x1 + dx[move]
            ny1 = y1 + dy[move]
            nx2 = x2 + dx[move]
            ny2 = y2 + dy[move]

            next_block1 = check_block(nx1, ny1)
            next_block2 = check_block(nx2, ny2)

            if next_block1 and next_block2:
                queue.append((nx1, ny1, nx2, ny2, cnt + 1))
            elif next_block1:
                queue.append((nx1, ny1, x2, y2, cnt + 1))
            elif next_block2:
                queue.append((x1, y1, nx2, ny2, cnt + 1))
    elif check1 or check2:
        answer = cnt
        break
    else:
        continue

print(answer)