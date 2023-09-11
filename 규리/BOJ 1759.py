def subset(N, i):
    global M, J, code
    if i == N:
        # 부분집합 원소 개수가 L개, 모음이 한개 이상, 자음이 한개 이상
        if sum(bits) == L and M >= 1 and J >= 2:
            # 사전순 정렬한 암호를 result 배열에 담기
            code.sort()
            cd = ''.join(code)
            result.append(cd)
        return

    bits[i] = 1
    # alpha[i]가 모음이면 모음카운트(M) + 1, 자음이면 자음카운트(J) + 1
    if alpha[i] in 'aeiou':
        M += 1
    else:
        J += 1
    # code 배열에 alpha[i] 담기
    code.append(alpha[i])
    subset(N, i+1)

    bits[i] = 0
    # 모음 or 자음 카운트 - 1
    if alpha[i] in 'aeiou':
        M -= 1
    else:
        J -= 1
    # code 배열에 alpha[i] 빼주기
    code.pop(code.index(alpha[i]))
    subset(N, i+1)

L, C = map(int, input().split())  # L:암호개수, C:주어진 알파벳 개수
alpha = list(map(str, input().split()))
bits = [0]*C
M = J = 0  # 모음, 자음
code, result = [], []  # 한개짜리 암호 담을 code 배열, 가능한 모든 암호 담을 result 배열
subset(C, 0)
result.sort()  # 사전순 정렬
for x in result:
    print(x)
