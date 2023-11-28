import sys
input = sys.stdin.readline

N, prob_e, prob_w, prob_s, prob_n = map(int, input().split())

# 방문체크를 어떤식으로 ???
# N = 14이기 때문에 29*29 배열을 만들면 되지 않을까 .. ?
visited = [[0] * 29 for _ in range(29)]
visited[14][14] = 1
# porb 인자...
# 시작점, 이동경로 저장, 이동횟수, 
# # 모든 케이스 저장할 필요 x, 바로 계산
# cases = []
result = 0
arr = []
direct = ['N', 'E', 'S', 'W']
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def prob(start_x, start_y, arr, cnt):
    global result
    # 종료 조건
    if cnt == N:
        tmp = 1
        # arr를 확률로 환산
        for i in arr:
            if i == 'N':
                tmp *= prob_n/100
            elif i == 'E':
                tmp *= prob_e/100
            elif i == 'S':
                tmp *= prob_s/100
            else:
                tmp *= prob_w/100
        result += tmp
        return
    else:
        # 사방 탐색
        for i in range(4):
            nx = start_x + dx[i]
            ny = start_y + dy[i]
            if 0 <= nx < 29 and 0 <= ny < 29:
                if not visited[nx][ny]:
                    visited[nx][ny] = 1
                    arr.append(direct[i])
                    prob(nx, ny, arr, cnt + 1)
                    arr.pop()
                    visited[nx][ny] = 0


prob(14, 14, arr, 0)
print(result)
