# bfs
def solution(maps):
    from collections import deque
    import heapq
    answer = []
    li = len(maps)
    lj = len(maps[0])
    visited = [[0] * lj for _ in range(li)]
    # 순회하면서 X가 아니고 방문한적 없으면 bfs 진행
    for i in range(li):
        for j in range(lj):
            if maps[i][j] != "X" and visited[i][j] == 0:
                print(i, j)
                que = deque()
                que.append((i, j))
                visited[i][j] = 1
                meal = int(maps[i][j])
                while que:
                    x, y = que.popleft()
                    for dx, dy in [[0,1],[0,-1],[1,0],[-1,0]]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < li and 0 <= ny < lj and maps[nx][ny] != "X" and visited[nx][ny] == 0:
                            que.append((nx, ny))
                            visited[nx][ny] = 1
                            meal += int(maps[nx][ny])
                heapq.heappush(answer, meal)
    if not answer:
        answer.append(-1)
    return sorted(answer)
