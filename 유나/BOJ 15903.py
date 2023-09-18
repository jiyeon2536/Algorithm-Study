import sys
import heapq

# 계속 정렬하여 가장 작은 두 수를 합해야 함
input = sys.stdin.readline
n, m = map(int, input().strip().split())

# 데이터 입력 및 정렬
arr = sorted(list(map(int, input().strip().split())))

# heapq 사용
# 가장 작은 두 수 pop하여 더하고 다시 입력
for _ in range(m):
    num1 = heapq.heappop(arr)
    num2 = heapq.heappop(arr)
    plus = num1 + num2
    heapq.heappush(arr, plus)
    heapq.heappush(arr, plus)

print(sum(arr))
