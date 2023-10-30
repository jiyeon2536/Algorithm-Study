from collections import deque
# 메인로직
def main():
    q = deque()
    total = []
    for i in range(n+1):
        if arrlen[i] == 0:
            q.append(i)
    while q:
        a = q.popleft()
        total.append(a)
        if len(arr[a]) > 0:
            for i in range(len(arr[a])):
                arrlen[arr[a][i]] -= 1
                if arrlen[arr[a][i]] == 0:
                    q.append(arr[a][i])
    return total



# 인풋


n, m = map(int, input().split())
# n명의 학생 m은 키를 비교한 회수
arr = [[] for _ in range(n+1)]
arrlen = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arrlen[b] += 1




# 아웃풋
rs = main()
ru = rs[1:]
print(*ru)
