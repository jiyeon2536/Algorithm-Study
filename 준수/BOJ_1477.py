def binary_search():
    low = 1
    high = L + 1
    answer = -1

    while low <= high:
        mid = (low + high) // 2
        result = install(mid)

        if result <= M:
            high = mid - 1
            answer = mid
        else:
            low = mid + 1

    return answer


def install(max_dist):
    cnt = 0
    location = 0
    idx = 0

    while location < L:
        if idx < N and rest_area[idx] <= location + max_dist:
            location = rest_area[idx]
            idx += 1
        else:
            location += max_dist
            
            if location >= L:
                break
            
            cnt += 1

    return cnt

N, M, L = map(int, input().split())

rest_area = sorted(list(map(int, input().split())))

print(binary_search())