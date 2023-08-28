import sys
from collections import deque
input = sys.stdin.readline
N = int(input())

def BFS(s):
    queue = deque()
    queue.append(s)
    visited[s] = 1

    while queue:
        n = queue.popleft()
        for w in connection[n]:
            if visited[w] == 0:
                queue.append(w)
                visited[w] = 1
                par[w] = n

# 트리의 연결 정보
arr = [list(map(int, input().split())) for _ in range(N - 1)]

# BFS 를 위한 방문 표시 리스트
visited = [0] * (N + 1)

# 부모노드 저장 리스트
par = deque([0] * (N + 1))

# 각 노드에 연결 되어 있는 노드를 담을 리스트
connection = [[] for _ in range(N + 1)]

for i in range(len(arr)):
    connection[arr[i][1]].append(arr[i][0])
    connection[arr[i][0]].append(arr[i][1])

# 루트를 1로 설정하므로 1번 노드부터 BFS 시작하여 각 노드들의 부모노드 검색
BFS(1)

# 출력하기 편하게 0, 1 인덱스 요소 제거
par.popleft()
par.popleft()
while par:
    print(par.popleft())

