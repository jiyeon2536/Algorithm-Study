def inorder_traverse(n):
    global i
    if n * 2 <= len(arr):  # 범위내면 계속 왼쪽으로 간다. 끝에 다으면 벗어난다.
        inorder_traverse(n*2)
    s1[n] = arr[i]  # 왼쪽 끝에서 1 부여
    i += 1
    if n * 2 + 1 <= len(arr):  # 위와 같음
        inorder_traverse(n * 2 + 1)


# 중위 순회
K = int(input())
arr = list(map(int, input().split()))
s1 = [0] * (len(arr)+1)
i = 0
inorder_traverse(1)
degree = 0
start = 1
while degree < K:
    end = start + 2 ** degree
    for i in range(start, end):
        print(s1[i], end=' ')
    print()
    degree += 1
    start = end
