import sys
input = sys.stdin.readline

def is_prime(N):
    prime = [True]*(N+1)
    prime[0] = prime[1] = False

    for i in range(2, N+1):
        if prime[i]:
            for j in range(i*i, N+1, i):
                prime[j] = False
    return [i for i in range(N+1) if prime[i]]

N = int(input())
nums = is_prime(N)

start = end = cnt = 0
ans = 0
while end < len(nums):
    ans = sum(nums[start:end+1])
    if ans == N:
        cnt += 1
        start += 1
    elif ans > N:
        start += 1
    else:
        end += 1

print(cnt)
