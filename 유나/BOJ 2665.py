import heapq
import sys
input = sys.stdin.readline

def dijkstra():
    que = [(0, 0, 0)] # w, i, j
    inf = sys.maxsize
    # 최댓값 : 가중치를 변경 횟수로 두었음
    dist = [[inf] * n for _ in range(n)]
    dist[0][0] = 0

    while que:
        w, i, j = heapq.heappop(que)
        for di, dj in [[0,1],[0,-1],[1,0],[-1,0]]:
            ni, nj = i + di, j + dj
            # 범위 내에 존재한다면
            if 0 <= ni < n and 0 <= nj < n:
                # 그냥 지나갈 수 있다면 w 그대로 입력
                if arr[ni][nj] == 1:
                    new_cost = w
                    # 새로 계산한 값이 최솟값이면 갱신 후 que에 입력
                    if new_cost < dist[ni][nj]:
                        dist[ni][nj] = new_cost
                        heapq.heappush(que, (new_cost, ni, nj))
                else:
                    # 벽을 통과해야 하는 경우 w + 1
                    new_cost = w + 1
                    # 새로 계산한 값이 최솟값이면 갱신 후 que에 입력
                    if new_cost < dist[ni][nj]:
                        dist[ni][nj] = new_cost
                        heapq.heappush(que, (new_cost, ni, nj))
    return dist[n-1][n-1]


n = int(input().strip())
arr = [list(map(int, input().strip())) for _ in range(n)]

ans = dijkstra()
print(ans)
