def bfs(r, i):
    if r == 0:
        print(*reversed(comb)) 
        return

    for j in range(i, k - r + 1): # i부터 6자리만
        comb[r-1] = arr[j] # 자리 배정
        bfs(r-1, j+1) # 재귀


while True:
    arr = list(map(int, input().split()))
    k = arr.pop(0)
    if k == 0: # 0을 입력 받으면 멈춰라
        break
    comb = [0] * 6 # 6자리까지만 필요하기 때문에
    bfs(6, 0)
    print()
