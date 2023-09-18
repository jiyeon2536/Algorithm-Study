n, m = map(int, input().split())
nums = list(map(int, input().split()))

cnt = 0
while cnt != m:
    nums.sort()
    x = nums[0] + nums[1]
    nums[0] = nums[1] = x
    cnt += 1

print(sum(nums))
