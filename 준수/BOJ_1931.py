N = int(input())

tmp_end = -1
cnt = 0
arr = []

for i in range(N):
    start, end = map(int, input().split())
    arr.append((start, end))

arr.sort()
arr.sort(key=lambda x: x[1])

for j in arr:
    if j[0] >= tmp_end:
        tmp_end = j[1]
        cnt += 1

print(cnt)