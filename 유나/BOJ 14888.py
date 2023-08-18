def perm(i, n):
    global mx, mn
    # 기저조건
    if i == n: # 연산
        # 가지치기까진 못했고...
        # 중복되는 순열이 있다면 제외
        sum_v = num[0]
        for idx in range(len(opers)):
            if opers[idx] == '+':
                sum_v += num[idx+1]
            elif opers[idx] == '-':
                sum_v -= num[idx+1]
            elif opers[idx] == '*':
                sum_v *= num[idx+1]
            elif opers[idx] == '/': # 음수를 양수로 나누는 경우
                if sum_v < 0:
                    sum_v = -(-sum_v // num[idx+1])
                else:
                    sum_v //= num[idx+1]
        mx = max(mx, sum_v)
        mn = min(mn, sum_v)

    else:
        for j in range(i, n):
            opers[i], opers[j] = opers[j], opers[i]
            perm(i+1, n)
            opers[i], opers[j] = opers[j], opers[i]




n = int(input()) # 수의 개수
num = list(map(int, input().split()))
p, m, t, d = map(int, input().split()) # + - * // 의 개수
opers = ['+'] * p + ['-'] * m + ['*'] * t + ['/'] * d # 연산 기호


mx = -10**10
mn = 10**10

# 여러가지 연산 조합 뽑기
perm(0, n-1)
print(mx)
print(mn)
