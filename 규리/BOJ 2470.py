import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
nums.sort(key=lambda x:abs(x))

start, end = 0, 1
mn_abs = 10 ** 10
result = []
while True:
    if end == N:
        break
    ans = nums[start] + nums[end]
    if mn_abs > abs(ans):  # 0에 가까운 두 수 합 찾기 -> 절대값
        mn_abs = abs(ans)
        result = [nums[start], nums[end]]  # mn값, result 갱신
    start, end = start+1, end+1

result.sort()
print(*result)
