N = int(input())
arr = [0]
is_prime = [True] * (N + 1)
is_prime[0] = False
is_prime[1] = False

for n in range(2, N + 1):
    if is_prime[n]:
        arr.append(arr[-1] + n)
        m = 2

        while n * m <= N:
            is_prime[n * m] = False
            m += 1

i = 0
j = 1
cnt = 0

while j < len(arr):
    cur = arr[j] - arr[i]

    if cur == N:
        cnt += 1
        i += 1
    elif cur > N:
        i += 1
    else:
        j += 1

print(cnt)