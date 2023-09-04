import sys
input = sys.stdin.readline

N = int(input())

def find(s, e, n):
    global blue_cnt
    global white_cnt

    tmp = 0
    # 처음 find 함수 호출할 때 배열 전체를 호출
    for i in range(s, s + n):
        for j in range(e, e + n):
            if arr[i][j] == 1:
                tmp += 1
    # 각 위치의 값을 더한 tmp 값이 배열의 크기와 같다면
    if tmp == n ** 2:
        blue_cnt += 1
        return
    # tmp 값이 0 이라면
    elif tmp == 0:
        white_cnt += 1
        return

    # 둘 다 아니라면
    else:
        # 범위를 반으로 줄이고
        mid = n // 2
        # 네 사분면의 시작과 끝 범위를 재조정하여 재귀
        find(s, e, mid)
        find(s + mid, e,mid)
        find(s, e + mid, mid)
        find(s + mid, e + mid, mid)


arr = [list(map(int, input().split())) for _ in range(N)]

blue_cnt = 0
white_cnt = 0
find(0,0,N)
print(white_cnt)
print(blue_cnt)

