def installation(dist):
    cnt = 1
    prev = houses[0]
    idx = 0

    while True:
        idx += 1

        if idx >= N or cnt == C:
            break

        if houses[idx] >= prev + dist:
            prev = houses[idx]
            cnt += 1

    return cnt

def binary_search():
    low = 0
    high = 1000000000
    answer = -1

    while low <= high:
        mid = (low + high) // 2
        result = installation(mid)

        if result == C:
            low = mid + 1
            answer = mid
        elif result > C:
            low = mid + 1
        else:
            high = mid - 1

    return answer


N, C = map(int, input().split())
houses = []

for _ in range(N):
    x = int(input())
    houses.append(x)

houses.sort()

print(binary_search())