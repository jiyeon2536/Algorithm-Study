def boj8983():
    def binarySearch(arr, target):
        start, end = 0, len(arr) - 1
        while start <= end:
            mid = (start + end) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return end

    m, n, l = map(int, input().split())  # 사대의 수, 동물의 수, 사정거리
    x_arr = list(map(int, input().split()))  # 사대의 위치
    # 각 동물의 사는 위치
    anml = [list(map(int, input().split())) for _ in range(n)]
    # 사대의 위치와 동물의 위치 간의 거리는 abs(xi-aj) + bj
    # 이분 탐색..?
    # 가능한 사대를 for문을 다 돌지 않고 이분 탐색 으로 해결 한다
    x_arr.sort()
    anml.sort()
    cnt = 0
    for i in range(len(anml)):
        # 가장 가까운 사대의 인덱스를 찾아서 추가
        if anml[i][1] > l:
            continue
        idx = binarySearch(x_arr, anml[i][0])
        ans_left = abs(anml[i][0] - x_arr[idx]) + anml[i][1]
        ans_right = abs(anml[i][0] - x_arr[idx + 1]) + anml[i][1] if idx < m - 1 else float('inf')
        ans = min(ans_right, ans_left)
        
        if ans <= l:
            cnt += 1
        
    print(cnt)


boj8983()
