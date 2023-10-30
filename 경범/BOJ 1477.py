# 메인 로직
def main():
    start = 1
    end = l - 1
    rst = 0
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] > mid:
                cnt += (arr[i] - arr[i-1]-1) // mid

        if cnt > m:
            start = mid + 1
        else:
            end = mid - 1
            rst = mid
    return rst




# 인풋
n, m , l = map(int, input().split())
# n = 휴게소 개수 m= 더 지으려는 휴게소 l = 고속도로 거리
arr = list(map(int, input().split()))
arr.append(0)
arr.append(l)
arr.sort()



# 아웃풋
rs = main()
print(rs)

