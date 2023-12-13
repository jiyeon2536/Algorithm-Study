# py.py에서만 돌아가고 python으로 하면 시간초과 남
N = int(input())
arr = list(map(int, input().split()))
oper = list(map(int, input().split()))
# 숫자는 고정하고 오퍼레이터를 순열 돌린다.
stack = []
if oper[0] > 0:
    for i in range(oper[0]):
        stack.append('+')
if oper[1] > 0:
    for i in range(oper[1]):
        stack.append('-')
if oper[2] > 0:
    for i in range(oper[2]):
        stack.append('*')
if oper[3] > 0:
    for i in range(oper[3]):
        stack.append('/')
# 스택에 사칙연산 넣기
#print(stack)
# +, -, *, /
# 완전 탐색
# 숫자 하나 oper하나 나와야 한다.
mi = 1000000000  # 최솟값
mx = -1000000000  # 최댓값
res = []


def f(i, N, sv):
    global mx
    global mi
    if i == len(stack):  # 스택의 길이와 같아지면 DFS끝난 것
        for k in range(len(stack)):
            if stack[k] == '+':
                sv += arr[k+1]
            elif stack[k] == '-':
                sv -= arr[k+1]
            elif stack[k] == '*':
                sv *= arr[k+1]
            elif stack[k] == '/':  # 나눗셈은 C++형태를 따른다.
                if sv < 0:
                    sv = -sv        # 음수일 떄 양수로 바꾸고
                    sv //= arr[k+1]  # 몫만 챙긴다.
                    sv = -sv
                else:
                    sv //= arr[k+1]
        mx = max(mx, sv)
        mi = min(mi, sv)
    else:
        for j in range(i, len(stack)):  # 사칙연산으로 순열 돌린다.
            stack[i], stack[j] = stack[j], stack[i]
            f(i+1, N, sv)
            stack[i], stack[j] = stack[j], stack[i]
            sv = arr[0]


f(0, N, arr[0])
print(mx, mi)
