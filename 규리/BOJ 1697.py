# 1697 숨바꼭질

from collections import deque

def f(N):
    global time
    visited = [0]*100001
    q = deque()
    q.append(N)
    while q:
        n = q.popleft()
        if n == K:
            result = visited[n]
            break
        for k in [n-1, n+1, n*2]:
            if 0 <= k <= 100000 and visited[k] == 0:
                visited[k] = visited[n] + 1
                q.append(k)
    return result

N, K = map(int, input().split())
time = 0
print(f(N))
