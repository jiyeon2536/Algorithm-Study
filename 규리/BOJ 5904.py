N = int(input())

# total:총 길이 / moo:중간 moo 길이 / N:찾는 인덱스
def Moo(total, moo, N):
    if N <= 3:
        return "moo"[N-1]

    left = (total - moo) // 2

    if N <= left:  # moo 왼쪽
        return Moo(left, moo-1, N)
    elif N > left + moo:  # moo 오른쪽
        return Moo(left, moo-1, N-left-moo)
    else:  # 중간 moo 사이에 N이 있을 때  -->  left < N <= left + moo
        if N - left == 1:
            return "m"
        else:
            return "o"

length = 3
moo = 0
while length < N:
    moo += 1
    length = 2*length + (moo + 3)

print(Moo(length, moo+3, N))
