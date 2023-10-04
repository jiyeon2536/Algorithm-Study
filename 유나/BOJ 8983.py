'''
사냥꾼
거리 : abs(x-a) + b
- 동물들의 위치를 순회하면서 사냥될지 아닌지 체크
- 일단 동물의  y좌표 사정 거리 이내가 아니라면 이분탐색 진행하지 않음
'''
import sys
input = sys.stdin.readline

# 왼쪽, 오른족 끝값, 동물들의 좌표
def binary(left, right, x, y):
    global res
    # 사냥되지 않는 위치라면 return
    if right < left:
        return
    # 중간 인덱스 구하기
    mid = (left + right) // 2
    
    # abs(arr[mid])-x) + y <= l 이라면 res + 1
    if abs(arr[mid] - x) <= l - y:
        res += 1
    # 동물의 위치가 중앙값보다 왼쪽이라면, (0, mid-1)
    elif arr[mid] > x:
        binary(0, mid-1, x, y)
    # 동물의 위치가 중앙값보다 오른쪽이라면 (mid +1, right)
    else:
        binary(mid+1, right, x, y)

# 사대의 수, 동물의 수, 사정 거리
m, n, l = map(int, input().strip().split())
arr = list(map(int, input().strip().split())) # 사대의 좌표
arr.sort()
res = 0 # 사냥한 동물의 수

for _ in range(n):
    x, y = map(int, input().strip().split())

    # y가 사정거리 이상이라면 넘기기
    if y > l:
        continue
        
    # 이분 탐색 진행
    left = 0
    right = m - 1
    binary(left, right, x, y)
print(res)
