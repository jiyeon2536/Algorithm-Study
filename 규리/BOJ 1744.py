N = int(input())
nums = [int(input()) for _ in range(N)]
nums.sort(reverse=True)
result = 0

idx = 0
for i in range(N):
    if nums[i] < 0:
        idx = i
        break
check = True  # 음수인 정수가 짝수 개
if len(nums[idx:]) % 2 == 1:
    check = False  # 음수인 정수가 홀수 개

i = 0
while True:
    if i == N-1:
        result += nums[i]
        break
    elif i > N-1:
        break
        
    if nums[i] > 0:
        if nums[i+1] > 0:
            if nums[i+1] != 1:
                result += nums[i] * nums[i+1]
            else:
                result += nums[i] + 1
            i += 2
        elif nums[i+1] <= 0:
            result += nums[i]
            i += 1
    elif nums[i] == 0:
        if len(nums[i+1:]) % 2 == 0:
            i += 1
        else:
            i += 2
    else:  # nums[i] < 0
        if check == True:
            result += nums[i] * nums[i+1]
            i += 2
        else:
            if i == idx:
                result += nums[i]
                i += 1
                continue
            else:
                result += nums[i] * nums[i+1]
                i += 2
print(result)
