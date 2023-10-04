def boj1780():
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 만약 종이가 모두 같은 수로 되어 있다면 이 종이를 그대로 사용 한다.
    # 같은 수가 아니라면 종이를 같은 크기의 종이 9개로 짜르고 잘린 종이에 대해서 1의 과정을 반복한다.
    # -1, 0, 1 로만 채워진 종이의 개수를 구해내는 프로그램을 작성하시오
    # arr을 계속 돌면 안된다.
    mis = 0
    zro = 0
    pls = 0


    def chk(r, c, n):
        nonlocal mis, zro, pls
        col = arr[r][c]  # 현재 색상
        for i in range(r, r+n):
            for j in range(c, c+n):
                if arr[i][j] != col:
                    nn = n // 3
                    chk(r, c, nn)
                    chk(r, c + nn, nn)
                    chk(r, c + 2 * nn, nn)
                    chk(r + nn, c, nn)
                    chk(r + 2 * nn, c, nn)
                    chk(r + nn, c + nn, nn)
                    chk(r + nn, c + 2 * nn, nn)
                    chk(r + 2 * nn, c + nn, nn)
                    chk(r + 2 * nn, c + 2 * nn, nn)
                    return
        if col == -1:
            mis += 1
        elif col == 0:
            zro += 1
        elif col == 1:
            pls += 1
    chk(0, 0, N)
    print(f'{mis}\n{zro}\n{pls}\n')


boj1780()
