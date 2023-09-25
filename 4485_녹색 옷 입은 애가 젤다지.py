import sys
input = sys.stdin.readline
import heapq

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def dijkstra():
    min_heap = [(cave[0][0], 0, 0)]
    black_rupee = [[float('inf')] * N for _ in range(N)]

    while min_heap:
        current_minus, x, y = heapq.heappop(min_heap)
        if x == N - 1 and y == N - 1:
            print(f'Problem {tc}: {black_rupee[y][x]}')
            return
        for direction in range(4):
            nx, ny = x + dx[direction], y + dy[direction]
            if 0 <= nx < N and 0 <= ny < N:
                calculated = current_minus + cave[ny][nx]
                if black_rupee[ny][nx] > calculated:
                    black_rupee[ny][nx] = calculated
                    heapq.heappush(min_heap, (calculated, nx, ny))
                    
tc = 0
while True:
    N = int(input())
    if N == 0:
        break
    tc += 1
    cave = [list(map(int, input().split())) for _ in range(N)]
    dijkstra()