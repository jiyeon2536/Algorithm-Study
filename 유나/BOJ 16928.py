import sys
input = sys.stdin.readline
from collections import deque

'''
뱀과 사다리 게임
주사위 : 1~6 / 10x10 보드판 1~100
i번칸, 4가 나오면 i+4번칸으로 이동 , 100 이상이된다면 이동할 수 없음
사다리라면 사다리 타고 이동, 뱀이 있다면 뱀을 따라 내려간다
사다리 => 이동한 칸의 번호가 원래 있던 간의 번호보다 크고
뱀 => 디옹한 칸의 번호가 원래 있던 칸의 번호보다 작음

1에서 시작하여 100번 칸에 도착 : 주사위를 굴려야 하는 횟수의 최솟값

'''


def bfs():
    que = deque()
    que.append(1)
    visited = [0] * 101

    while que:
        i = que.popleft()
        if i == 100:
            return visited[100]

        for k in range(1, 7):
            ni = i + k
            if ni <= 100 and visited[ni] == 0:
                if ladder.get(ni, False):
                    if visited[ladder[ni]] == 0:
                        que.append(ladder[ni])
                        visited[ladder[ni]] = visited[i] + 1
                elif snake.get(ni, False):
                    if visited[snake[ni]] == 0:
                        que.append(snake[ni])
                        visited[snake[ni]] = visited[i] + 1
                else:
                    que.append(ni)
                    visited[ni] = visited[i] + 1
    return visited[100]


# 사다리의 수, 뱀의 수
n, m = map(int, input().strip().split())

# 사다리 정보
ladder = dict()
for _ in range(n):
    x, y = map(int, input().strip().split())
    ladder.setdefault(x, y)

# 뱀의 정보
snake = dict()
for _ in range(m):
    u, v = map(int, input().strip().split())
    snake.setdefault(u, v)
res = bfs()
print(res)

