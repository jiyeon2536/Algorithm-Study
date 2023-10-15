def div(paper, num, x, y):
    global minus
    global zero
    global plus

    if num == 0:
        return False

    tmp = num // 3

    moe = 0
    zro = 0
    one = 0

    for n in range(x, x + num):
        for m in range(y, y + num):
            if paper[n][m] == -1:
                moe += 1
            elif paper[n][m] == 0:
                zro += 1
            else:
                one += 1

    if zro == num * num:
        zero += 1
    elif one == num * num:
        plus += 1
    elif moe == num * num:
        minus += 1
    else:
        for i in range(x, x + num, tmp):
            for j in range(y, y + num, tmp):
                div(paper, tmp, i, j)


N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

minus = 0
zero = 0
plus = 0

div(paper, N, 0, 0)

print(minus, zero, plus, sep="\n")
