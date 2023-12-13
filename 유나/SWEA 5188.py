def dfs(i, j, s):
    global mn
    # 마지막 인덱스에 도착하면 mn 갱신
    if i == n-1 and j == n-1:
        mn = min(mn, s)

    # 가지치기 합이 mn보다 커지면 끝내기
    if s > mn:
        return
    
    # 오른쪽 , 아래 방향 탐색
    for di, dj in [[0,1], [1,0]]:
        ni = i + di
        nj = j + dj
        # 인덱스 내에 존재한다면 dfs 진행
        if 0 <= ni < n and 0 <= nj < n:
            dfs(ni, nj, s + arr[ni][nj])

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    mn = 100000
    dfs(0, 0, arr[0][0])
    print(f'#{tc} {mn}')
