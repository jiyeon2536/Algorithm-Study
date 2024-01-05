def solution(grid):
    answer = []
    n = len(grid)
    m = len(grid[0])
    visited = [[[0 for _ in range(4)] for _ in range(m)] for _ in range(n)]
    # print(visited)
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    def find(i, j, k):
        nonlocal cnt, visited, n, m, answer
        while not visited[i][j][k]:
            visited[i][j][k] = 1
            cnt += 1
            i = (i + dx[k]) % n
            # 회전하는거 dx, dy값의 순서에 영향 받음...
            j = (j + dy[k]) % m
            if grid[i][j] == 'R':
                k = (k + 1) % 4
            elif grid[i][j] == 'L':
                k = (k - 1) % 4
            # print(i, j, k)
        # print(visited)
        # print("find 끝남")
        answer.append(cnt)
    for ii in range(n):
        for jj in range(m):
            for kk in range(4):
                if not visited[ii][jj][kk]:
                    cnt = 0
                    i, j, k = ii, jj, kk
                    find(i, j, k)
    answer.sort()
    return answer
