n= int(input())
cnt = 0
a = [False,False] + [True]*(n-1)
primes=[0] # 소수리스트

for i in range(2,n+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False


arr = [] # 누적합
c = 0
for i in range(len(primes)):
    c += primes[i]
    arr.append(c)

start = 0
end = 0

while end < len(arr):
    if arr[end] - arr[start] >= n:
        if arr[end] - arr[start] == n:
            cnt += 1
        start += 1
    else:
        end += 1

print(cnt)




