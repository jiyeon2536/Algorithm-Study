def boj1477():
    N, M, L = map(int, input().split())
    # N = 현재 휴게소 개수
    # M = 더 지으려는 휴게소의 개수
    # L = 고속도로의 길이
    rest = list(map(int, input().split()))
    rest.append(0)
    rest.append(L)
    rest.sort()
    # 현재 휴게소의 위치
    # 휴개소 간의 거리를 이분탐색으로 결정한다?
    # 거리로 리스트를 만든 다음에 최댓 값을 M만큼 나눈다?
    # --> x 답이 안나옴

    # 설치해야 할 휴게소 개수가 M보다 크다면 mid는 더 길어야 한다
    # 설치해야 할 휴게소 개수가 M보다 작다면 mid는 더 짧아야 한다.(조건을 만족하는 경우!)
    def binarySearch(arr, start, end):
        res = 0
        while start <= end:
            cnt = 0
            mid = (start + end) // 2
            for i in range(1, len(arr)):
                if arr[i] - arr[i - 1] >= mid:
                    cnt += (arr[i] - arr[i - 1] - 1) // mid
            if cnt > M:
                start = mid + 1
            else:
                end = mid - 1
                res = mid
        return res
    print(binarySearch(rest, 1, L-1))


boj1477()
