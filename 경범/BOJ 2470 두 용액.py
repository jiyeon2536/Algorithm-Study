# 메인로직
def bs(arr, key, i):
    start = i
    end = len(arr)
    cnt = 1e9
    while start <= end:
        mid = (start + end) // 2
        if abs(arr[mid] + arr[key]) == 0:
            cnt = arr[mid]
            return cnt
        else:
            if arr[mid] + arr[key] > 0:
                end = mid - 1
                if cnt > arr[mid]:
                    cnt = arr[mid]
            elif arr[mid] + arr[key] < 0:
                start = mid + 1
                if cnt > arr[key]:
                    cnt = arr[mid]
         # arr[key] + arr[mid]절댓값이 0과 가장 가까울 때의
        # mid 값을 cnt 저장하겠다
    return cnt


def fun():
    total = []
    cnt = int(1e9)
    for i in range(len(arr)):
        key = arr[i]
        rs = bs(arr, key, i)
        if cnt > rs + key:
            cnt = rs + key
            total = [rs, key]
    return total



# 인풋
n = int(input())
arr = list(map(int, input().split()))
arr.sort()




# 아웃풋
rs = fun()
print(rs)

