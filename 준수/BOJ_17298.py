N = int(input())
arr = list(map(int, input().split()))
stack = []
answer = [-1] * N

for idx in range(N):
    if stack:
        prev_idx = stack[-1]

        while arr[prev_idx] < arr[idx]:
            answer[prev_idx] = arr[idx]
            stack.pop()

            if stack:
                prev_idx = stack[-1]
            else:
                break

        stack.append(idx)
    else:
        stack.append(idx)

print(*answer)