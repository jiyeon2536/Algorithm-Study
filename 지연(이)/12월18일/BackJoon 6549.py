# 히스토그램에서 가장 큰 직사각형

import sys
input = sys.stdin.readline

def solution(N,arr):
    answer = 0
    stack = []

    for i in range(N):
        if not stack or (stack[-1][1]<arr[i]):
            stack.append((i,arr[i]))
        else:
            while stack:
                if stack[-1][1]<=arr[i]:
                    stack.append((i,arr[i]))
                    break
                idx,value = stack.pop()
                if stack:
                    answer = max(answer, (i-stack[-1][0]-1)*value)
                else:
                    answer = max(answer, i*value)
            if not stack:
                stack.append((i,arr[i]))
        # print(f'stack:{stack} answer:{answer}')

    i = N
    while stack:
        idx,value = stack.pop()
        if stack:
            answer = max(answer, (i-stack[-1][0]-1)*value)
        else:
            answer = max(answer, i*value)
        # print(f'stack:{stack}, answer:{answer}')

    return answer


while True:
    N, *arr = list(map(int, input().split()))
    if N==0: break
    print(solution(N,arr))


# 반례
# 10 2 3 4 5 0 7 6 5 4 3
# 8 1 2 3 4 5 6 7 8
# 8 8 7 6 5 4 3 2 1
# 3 2 1 2
# 5 2 1 1 1 2

# 정답
# 16
# 20
# 20
# 3
# 5
