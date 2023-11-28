N = int(input())  # 진주알 개수
p = list(map(int, input().split()))  # 진주알 가치
p.sort()

result = 0
arr = [p[0]]
for i in range(1, N):
    if i % 2 == 0:
        result += p[i]*arr[-1]
        arr.append(p[i])
    else:
        result += p[i]*arr[0]
        arr.insert(0, p[i])

result += arr[-1] * arr[0]
print(result)
print(*arr)
