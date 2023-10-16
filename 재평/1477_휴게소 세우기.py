import sys
input = sys.stdin.readline

N, M, L = map(int, input().split())
highway = [0]
highway.extend(list(map(int, input().split())))
highway.append(L)
highway.sort()

start = 1
end = L - 1
while start <= end:
    rest = 0
    mid = (start + end) // 2
    for i in range(1, len(highway)):
        if highway[i] - highway[i-1] > mid:
            rest += (highway[i] - highway[i-1] - 1)//mid
    if rest <= M:
        end = mid - 1
        answer = mid
    else:
        start = mid + 1
print(answer)