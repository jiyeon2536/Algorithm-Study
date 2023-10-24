def boj1644():
    N = int(input())
    prime = []
    s, e = 0, 0
    for i in range(2, N+1):
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                break
        else:  # for문에 안 걸렸으면 소수다.
            prime.append(i)
    if N == 1:
        print(0)
        return
    sv = prime[0]
    cnt = 0
    while True:
        if sv < N:
            e += 1
            if e == len(prime):
                break
            sv += prime[e]
        else:
            if sv == N:
                cnt += 1
            sv -= prime[s]
            s += 1
    print(cnt)

boj1644()
