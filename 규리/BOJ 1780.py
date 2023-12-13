def paper(x, y, n):
    global result
    v = arr[x][y]
    cnt = 0

    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] == v:
                cnt += 1

    if cnt == n**2:  # 모든 칸이 같은 값
        if v == -1:
            result[0] += 1
        elif v == 0:
            result[1] += 1
        elif v == 1:
            result[2] += 1
        return
    else:
        z = n//3
        # 9 칸으로 나눠서 재귀
        paper(x, y, z)
        paper(x, y+z, z)
        paper(x, y+2*z, z)
        paper(x+z, y, z)
        paper(x+z, y+z, z)
        paper(x+z, y+2*z, z)
        paper(x+2*z, y, z)
        paper(x+2*z, y+z, z)
        paper(x+2*z, y+2*z, z)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
result = [0, 0, 0]  # -1, 0, 1 개수 카운팅
paper(0, 0, N)
for res in result:
    print(res)
