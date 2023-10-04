import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # N:도시개수 / M:버스노선개수
graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B, C = map(int, input().split())  # A:시작도시 / B:도착도시 / C:이동시간
    graph[A].append((B, C))

arr = []
time = [float('inf')] * (N+1)

def bellman_ford(graph, start):
    for a in range(N+1):
        for b, c in graph[a]:
            arr.append((a, b, c))

    time[start] = 0

    for _ in range(N-1):
        for a, b, c in arr:
            new_time = time[a] + c
            if time[b] > new_time:
                time[b] = new_time
    return time

start = 1
result = bellman_ford(graph, start)

check = True
for a, b, c in arr:
    if time[b] > time[a] + c:
        check = False
        break
if check == False:
    print(-1)
else:
    for res in result[2:]:
        if res == float('inf'):
            print(-1)
        else:
            print(res)
