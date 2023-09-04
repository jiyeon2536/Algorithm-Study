def div(paper, num, x, y):
    global white
    global blue

    # 더 이상 색종이를 자를 수 없으면 멈춰!
    if num == 0:
        return 0

    # 자주 쓰는 연산값을 임시 변수에 할당
    tmp = num // 2

    # 색종이에 흰색과 파란색이 몇 개?
    w = 0
    b = 0

    # 하나하나 세아려보면 알지!
    for n in range(x, x + num):
        for m in range(y, y + num):
            if paper[n][m]:
                b += 1
            else:
                w += 1

    # 이 색종이에 하나의 색만 있다면 더 이상 자르지 않음
    if w == num * num:
        white += 1
    elif b == num * num:
        blue += 1
    else:
        # 색이 섞여 있다면 다시 4개의 색종이로 잘라서 확인
        for i in range(x, x + num, tmp):
            for j in range(y, y + num, tmp):
                div(paper, tmp, i, j)

import sys
input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

white = 0
blue = 0

div(paper, N, 0, 0)
print(white, blue)