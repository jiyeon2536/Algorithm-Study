'''
투 포인터 2가지 방식
- 앞에서 시작하는 포인터와 끝에서 시작하는 포인터
- 빠른 포인터(fast runner)가 느린 포인터(slow runner)보다 앞서는 형식
'''
import sys
input = sys.stdin.readline

n = int(input().strip())
arr = list(map(int, input().strip().split()))

# 투 포인터 사용을 위한 정렬
arr.sort()

# 시작점과 끝점
start = 0
end =  len(arr)-1

# 절댓값의 최솟값을 구하기 때문에, 큰 값으로 초기값 설정
res = sys.maxsize

# start가 end보다 작을 동안에
while start < end:
    # start와 end 합의 절댓값이
    # res 값보다 작다면, rs, re, res 갱신
    if abs(arr[start] + arr[end]) < res:
        rs, re = start, end
        res = abs(arr[start] + arr[end])

    # 다음에 옮기 포인터 위치 결정
    # start를 옮겼을 때와, end를 옮겼을 때를 비교
    # 더 작은 res값을 가질 수 있도록 포인터 옮김
    if abs(arr[start+1] + arr[end]) > abs(arr[start] + arr[end-1]):
        end -= 1
    else:
        start += 1

print(arr[rs], arr[re])
