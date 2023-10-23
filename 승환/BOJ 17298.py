def boj17298():
    N = int(input())
    arr = list(map(int, input().split()))
    # 수열의 각 원소에 대해서 오른쪽에 있으면서 Ai 보다 큰 수 중에서 가장 왼쪽에 있는 수
    # 없으면 -1
    stack = []
    res = []
    for i in range(N-1, -1, -1):
        while stack:
            if stack[-1] <= arr[i]:
                stack.pop(-1)
            elif arr[i] < stack[-1]:
                res.append(stack[-1])
                stack.append(arr[i])
                break
        else:
            res.append(-1)
            stack.append(arr[i])
    for i in range(N-1, -1, -1):
        print(res[i], end=' ')


boj17298()
