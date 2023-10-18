from collections import deque
import heapq
import sys
input = sys.stdin.readline

def topological_sort():
    result = [] # 결과 리스트
    que = deque()
    # 진입 차수가 0인 학생(노드) que에 입력
    for idx in range(1, n+1):
        if arr[idx] == 0:
            que.append(idx)
    while que:
        k = que.popleft()
        result.append(k)
        # 해당 노드에서 갈 수 있는 노드 진입차수 1씩 빼주기
        for i in graph[k]:
            arr[i] -= 1
            # 진입 차수가 0이 된다면 que에 입력
            if arr[i] == 0:
                que.append(i)

    print(*result)

# 학생 수(노드 수), 비교 횟수(엣지 수)
n, m = map(int, input().strip().split())
graph = [[] for _ in range(n+1)] # 인접리스트, 번호가 1부터 시작하므로 n+1개
arr = [0] * (n+1) # 진입 차수

for _ in range(m):
    a, b = map(int, input().strip().split())
    graph[a].append(b) # a의 이동방향
    arr[b] += 1 # b의 진입차수 1 더해주기



topological_sort()
