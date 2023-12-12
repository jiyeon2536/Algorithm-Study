from collections import  deque
d = [(0,1),(0,-1),(1,0),(-1,0)]
def bfs(sx,sy,arr):
    # print('bfs')
    # print((sx,sy),arr)
    q = deque([(sx,sy)])
    visit = [[0]*5 for _ in range(5)]
    visit[sx][sy]=1
    while q:
        x,y = q.popleft()
        for dx,dy in d:
            nx = x + dx
            ny = y + dy
            if 0<=nx<5 and 0<=ny<5 and not visit[nx][ny]:
                if arr[nx][ny]=='P':
                    visit[nx][ny] = visit[x][y] + 1
                    if visit[nx][ny]-visit[sx][sy]<=2:
                        # print()
                        # print((sx,sy),0)
                        # for v in visit:
                        #     print(*v)
                        return 0
                elif arr[nx][ny]=='O':
                    visit[nx][ny] = visit[x][y] + 1
                    if visit[nx][ny]-visit[sx][sy]<=2:
                        q.append((nx,ny))

    # print()
    # print((sx,sy),1)
    # for v in visit:
    #     print(*v)
    return 1


def solution(places):
    answer = []
    for k in range(5):
        P = []
        for i in range(5):
            for j in range(5):
                if places[k][i][j]=='P':
                    P.append((i,j))
        cnt = len(P)
        for x,y in P:
            if bfs(x,y,places[k]):
                cnt-=1
        if cnt:
            answer.append(0)
        else:
            answer.append(1)
    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
                ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
                ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
# 대기실 1개
# print(solution(["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"]))
# print(solution(["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"]))
# print(solution(["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"]))
# print(solution(["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]))
