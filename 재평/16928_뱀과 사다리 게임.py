import sys
input = sys.stdin.readline
from collections import deque

# 1-6 주사위를 굴려 1-100까지의 마지막 칸인 100번에 도달하는 것이 목적
# 사다리 -> 올라감, 뱀 -> 내려감
# 정확히 100번 칸에 도착해야한다. 주사위 이동 값이 100을 초과할 경우 이동하지 않는다
# 100번칸에 도착하기 위해 가능한 최소 주사위 횟수 ...

# 사다리 수: 1 <= N <= 15, 뱀의 수: 1 <= M <= 15
N, M = map(int, input().split())
# 돌려돌려 주사위 횟수 정보 저장
cnt = [0] * 101
# BFS니깐 중첩 멈춰 방문 정보
its_visited = [0] * 101
# 사다리와 뱀 정보 입력
ladder = {}
snake = {}
for _ in range(N):
    # 사다리 정보 x -> y
    x, y = map(int, input().split())
    ladder[x] = y
for _ in range(M):
    # 뱀 정보 u -> v
    u, v = map(int, input().split())
    snake[u] = v

# 내가 졌다 난 BFS다...
# ----------------- BFS -----------------
player = deque([1])
# 최소 주사위 횟수를 구하는 로직 ...
# 도달하기까지 필요한 최소 주사위 횟수를 저장하는 배열 생성
# cnt = [float('inf')] * 101
dice = range(1, 7)
while player:
    start = player.popleft()
    # 종점 도착
    if start == 100:
        print(cnt[100])
        # 난 여기서 나간다 ㅅㄱ
        break
    for scale in dice:
        # 주사위 이동
        move_into = start + scale
        # RG ?
        if move_into <= 100 and not its_visited[move_into]:
            # 무야옹 ~ ! 사다리 !
            if move_into in ladder:
                move_into = ladder[move_into]
            # 뭬옹 ~ ㅠㅠ 뱀 !
            if move_into in snake:
                move_into = snake[move_into]
            # 얏홍
            if not its_visited[move_into]:
                its_visited[move_into] = 1
                cnt[move_into] = cnt[start] + 1
                player.append(move_into)

# # 난 DFS로 간다
# def DFS(start, dice_cnt):
#     if start == 0 or cnt[start] <= dice_cnt or start > 100:
#         return
#     for i in dice:
#         cnt[start+i] = min(cnt[start+i], dice_cnt)
#         DFS(board[start+i], dice_cnt+1)
# DFS(1, 1)
# 
# print(cnt[100])
