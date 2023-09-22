# 알고리즘 수업 - 병합 정렬 2
import sys
input = sys.stdin.readline

def merge_sort(arr, k):
    def divide(left, right):
        global cnt
        nonlocal arr
        # 쪼갤 것이 2개 이상 남이있을 떄까지
        if right - left < 2:
            return
        # left에서 right 범위가 홀수일 때 3 / 2 이렇게 나누어져야함
        mid = (left + right) // 2 + ((right - left) % 2)
        divide(left, mid)
        divide(mid, right)

        # 주어진 변경 횟수만큼 변경 했다면, return
        if cnt == k:
            return
        # 아니라면 돌려 ~
        merge(left, mid, right)

    def merge(left, mid, right):
        nonlocal arr, k
        global cnt
        i, j = left, mid
        
        # 정렬한 값을 받을 merged_arr 생성
        merged_arr = []
        while i < mid and j < right:
            if arr[i] < arr[j]:
                merged_arr.append(arr[i])
                i += 1
            else:
                merged_arr.append(arr[j])
                j += 1
        
        # 남은 요소 다 넣어주기
        merged_arr += arr[i:mid]
        merged_arr += arr[j:right]
        
        # left-right 범위 만큼 arr 변경해주기 위하여
        # left부터 right까지 값 변경
        i = left
        idx = 0
        while i < right:
            arr[i] = merged_arr[idx]
            i += 1
            idx += 1
            # 변경 횟수 세기
            cnt += 1
            
            # 변경 횟수를 만족한다면 return
            if cnt == k:
                return

    left = 0
    right = len(arr)
    return divide(left, right)

n, k = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
cnt = 0
merge_sort(arr, k)

# 변경횟수만큼 돌아서 반환된 것이면 
# 지금까지 저장된 arr 출력 아니라면 -1 출력
if cnt == k:
    print(*arr)
else:
    print(-1)
