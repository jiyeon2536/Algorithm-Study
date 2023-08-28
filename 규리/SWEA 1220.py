# 1220 Magnetic

T = 10
for tc in range(1, T+1):
    N = int(input())  # 정사각형 테이블 한변 길이 (항상 100)
    table = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for j in range(N):
        txt = ''
        for i in range(N):
            if table[i][j] in [1, 2]:
                txt += str(table[i][j])
        cnt += txt.count('12')
    print(f'#{tc} {cnt}')
