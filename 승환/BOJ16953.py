# A를 B로 바꾸려고 한다.
# 가능한 연산은
# *2
# *10 +1
# 두가지 이다.
def f(b, sv, cnt, mi, res):
    cnt += 1
    if sv > b:
        return
    if sv == b:
        if mi > cnt:
            mi = cnt
            res.append(mi)
    else:
        sv1 = sv * 2  # *2를 해서 재귀 돌리는 경우
        f(b, sv1, cnt, mi, res)
        sv2 = (sv * 10)+1  # 뒤에 1을 붙이는 경우
        f(b, sv2, cnt, mi, res)


def coo():
    a, b = map(int, input().split())
    mi = 1000000001
    res = []
    f(b, a, 0, mi, res)
    # 다 넘길 필요는 없다. (b, 0)만 넘기고 나머지는 고정값, global변수를 적게 쓰기 위해 다 넘김
    if res:
        print(min(res))
    else:
        print(-1)
#coo()


