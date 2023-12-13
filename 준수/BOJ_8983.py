def binary_search(key):
    low = 0
    high = M - 1
    close = int(1e12)

    while low <= high:
        mid = (low + high) // 2
        close = min(close, abs(key - X[mid]))

        if X[mid] == key:
            return 0
        elif X[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return close

M, N, L = map(int, input().split())
X = sorted(list(map(int, input().split())))
cnt = 0

for _ in range(N):
    a, b = map(int, input().split())

    x = binary_search(a)

    dist = x + b

    if dist <= L:
        cnt += 1

print(cnt)