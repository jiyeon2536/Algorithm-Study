N, M = map(int, input().split())
MAX = float('inf')
graph = [[] * (N + 1) for _ in range(N + 1)]
mn_times = [MAX] * (N + 1)
mn_times[1] = 0

for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((C, B))

is_loop = False

for repeat in range(N):
    for vertex in range(1, N + 1):
        for next_time, next_vertex in graph[vertex]:
            if mn_times[next_vertex] > mn_times[vertex] + next_time:
                mn_times[next_vertex] = mn_times[vertex] + next_time

                if repeat == N - 1:
                    is_loop = True

if is_loop:
    print(-1)
else:
    for idx in range(2, N + 1):
        time = mn_times[idx]

        if time == MAX:
            print(-1)
        else:
            print(time)