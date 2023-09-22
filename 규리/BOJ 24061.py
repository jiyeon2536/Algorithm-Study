import sys
input = sys.stdin.readline

def merge(arr, p, q, r):
    global result, cnt
    tmp = []
    i, j = p, q+1
    while i <= q and j <= r:
        if arr[i] <= arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1
    while i <= q:
        tmp.append(arr[i])
        i += 1
    while j <= r:
        tmp.append(arr[j])
        j += 1
    i, t = p, 0
    while i <= r:
        arr[i] = tmp[t]
        i, t, cnt = i + 1, t + 1, cnt + 1
        if cnt == K:
            result = arr[::]

def merge_sort(arr, p, r):
    if p < r:
        q = (p+r)//2
        merge_sort(arr, p, q)
        merge_sort(arr, q+1, r)
        merge(arr, p, q, r)

N, K = map(int, input().split())  # 배열 A 크기 N, 변경 횟수 K
A = list(map(int, input().split()))
result, cnt = [], 0
merge_sort(A, 0, len(A)-1)

if len(result) > 0:
    print(*result)
else:
    print(-1)
