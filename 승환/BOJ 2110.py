def binarySerach(a, start, end):
    global ans
    while start < end:
        middle = (start+end)//2
        cnt = 1
        chk = a[0]
        for k in range(N):
            if a[k] - chk >= middle:
                cnt += 1
                chk = a[k]
        # 설치 간격을 이분 탐색으로 결정한다. 
        # 이걸 어케 생각하냐?
        if cnt >= C:
            ans = middle
            start = middle + 1
        elif cnt < C:
            end = middle


N, C = map(int, input().split())
arr = []
for i in range(N):
    t = int(input())
    arr.append(t)
arr.sort()
ans = 0
# 공유기의 개수가 2이면
if C == 2:
    print(arr[-1]-arr[0])
    # 그냥 바로 출력한다.
else:
    # 공유기의 개수가 2이상인 경우 이진탐색으로 중앙값을 찾는다.
    # 만약 N = 7 C = 3일경우 1,4,7
    # N = 7, C = 4 일 경우 1,3,5,7 에 설치한다.
    # C - 2 만큼 나누어서 이진 탐색을 실행하면 된다.
    binarySerach(arr, 1, arr[-1]-arr[0])
    print(ans)
