import sys
input = sys.stdin.readline
from collections import deque

def bfs(start, end, init):
    # 연산할 값과 연산 횟수를 함께 삽입
    queue = deque([[start, init]])

    while queue:
        num, cnt = queue.popleft()

        # 연산하기 전의 수가 목표보다 크면 백트래킹
        if num > end:
            continue

        # A가 처음으로 B가 된 경우
        if num == end:
            print(cnt)
            return

        # 2를 곱한 경우의 수
        if num * 2 < 1000000001:
            queue.append([num * 2, cnt + 1])

        # 1을 수의 가장 오른쪽에 추가한 경우의 수
        if num * 10 + 1 < 1000000001:
            queue.append([num * 10 + 1, cnt + 1])
    
    # 만들 수 없는 경우
    print(-1)


A, B = map(int, input().split())

bfs(A, B, 1)