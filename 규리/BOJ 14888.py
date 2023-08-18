N = int(input())  # 숫자 개수
nums = list(map(int, input().split()))  # 수식에 사용되는 숫자
oper1 = list(map(int, input().split()))  # + - * / 개수 -> ex) 2 0 1 0
oper2 = {0: '+', 1: '-', 2: '*', 3: '/'}

arr = []  # ['+', '+', '-', '*', '/']
for i in range(4):
    for _ in range(oper1[i]):
        arr.append(oper2[i])

mx = -1000000000
mn = 1000000000

# 계산
def calc(oper, nums):
    global mx, mn
    result = nums[0]

    for o in range(len(oper)):
        if oper[o] == '+':
            result = result + nums[o + 1]
        elif oper[o] == '-':
            result = result - nums[o + 1]
        elif oper[o] == '*':
            result = result * nums[o + 1]
        elif oper[o] == '/':
            result = int(result / nums[o + 1])
    if mx < result:
        mx = result
    if mn > result:
        mn = result


# 연산자 순열
def perm(i, N):  # i: 깊이 / N: 순열 만들 리스트 크기
    if i == N:
        calc(''.join(arr), nums)
        return
    for j in range(i, N):

        check = False
        for k in range(i, j):
            if arr[k] == arr[j]:
                check = True
                break
        if check == True:
            continue

        arr[i], arr[j] = arr[j], arr[i]
        perm(i + 1, N)
        arr[i], arr[j] = arr[j], arr[i]

perm(0, len(arr))

print(mx)
print(mn)
