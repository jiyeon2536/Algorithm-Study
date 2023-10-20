import heapq, sys
input = sys.stdin.readline

def bfs(start):
    heap = []
    # heap[0] = (시작지점 색 바꾼 횟수, 시작지점 i, 시작지점 j)
    heapq.heappush(heap, (0, start[0], start[1]))
    visited[start[0]][start[1]] = 1

    di, dj = [0, 1, 0, -1], [1, 0, -1, 0]


    while heap:
        b, i, j = heapq.heappop(heap)
        if i == N - 1 and j == N - 1:
            return b
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                if maze[ni][nj] == 0:
                    heapq.heappush(heap, (b + 1, ni, nj))

                else:
                    heapq.heappush(heap, (b, ni, nj))
                visited[ni][nj] = 1


N = int(input())
maze = [list(map(int, input().strip())) for _ in range(N)]

visited = [[0] * N for _ in range(N)]

print(bfs((0, 0)))