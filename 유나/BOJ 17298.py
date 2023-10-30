from collections import deque
import sys
input = sys.stdin.readline

n = int(input().strip())
arr = list(map(int, input().strip().split()))
res = [-1] * n
stack = deque()

for i in range(n):
    # top보다 작거나 같은 경우에만 stack에 입력
    # 인덱스로 스택에 입력
    if stack:
        if arr[stack[-1]] >= arr[i]:
            stack.append(i)
        else:
            # stack이 존재하는 동안
            while stack:
                # top이 new보다 작거나 같다면 pop
                if arr[stack[-1]] < arr[i]:
                    idx = stack.pop()
                    res[idx] = arr[i]
                # top이 더 크다면 break
                else:
                    break
            stack.append(i)
    else:
        stack.append(i)

print(*res)
