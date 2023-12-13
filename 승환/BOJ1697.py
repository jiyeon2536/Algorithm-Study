from collections import deque
import sys


def bfs(s, g):
    cnt = 0
    q = [(s, cnt)]
    q = deque(q)
    while q:
        x = q.popleft()
        cnt = x[1]
        visited[x[0]] = 1
        if x[0] == g:
            break
        else:
            cnt += 1
            if x[0] > g:  # g보다 크면 +, *는 필요없다.
                if x[0] - 1 == g:  # -1 이랑 같으면 스탑
                    break
                q.append((x[0] - 1, cnt))
            else:
                if 2 * x[0] == g or x[0] + 1 == g or x[0] - 1 == g:  # 결과값과 같으면 멈춰라
                    break
                if 100000 >= 2 * x[0] and visited[2 * x[0]] == 0:  # 범위내에서 방문 하지 않았다면
                    q.append((2 * x[0], cnt))
                if 100000 >= x[0]+1 and visited[x[0]+1] == 0:  # +1 한 값이
                    q.append((x[0]+1, cnt))
                if 100000 >= x[0]-1 >= 0 and visited[x[0]-1] == 0:  # 방문하지 않았다면
                    q.append((x[0]-1, cnt))
    print(cnt)


N, K = map(int, sys.stdin.readline().split())
res = []
visited = [0] * 100001
bfs(N, K)
