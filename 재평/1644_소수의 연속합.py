import sys
input = sys.stdin.readline

def add_prime(N):
    for num in range(3, N+1):
        keep = True
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                keep = False
                break
        if keep:
            prime.append(num)
N = int(input())
if N < 2:
    prime = []
else:
    prime = [2]

add_prime(N)

result = 0
left = 0
right = 0
while right <= len(prime):
    total = sum(prime[left:right])
    if total == N:
        result += 1
        right += 1
    elif total < N:
        right += 1
    else:
        left += 1

print(result)