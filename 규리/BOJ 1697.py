# 1697 숨바꼭질

from collections import deque

def bfs(N):
    visited = [0]*100001
    q = deque()
    q.append(N)

    while q:
        n = q.popleft()
        if n == K:
            return visited[n]
        for i in [n-1, n+1, 2*n]:
            if 0 <= i <= 100000 and visited[i] == 0:
                visited[i] = visited[n] + 1
                q.append(i)

N, K = map(int, input().split())
print(bfs(N))
