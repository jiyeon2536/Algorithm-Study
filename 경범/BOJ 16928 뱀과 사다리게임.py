from collections import deque
# 메인로직

def sol(start):
    queue = deque()
    mat[start] = 0
    queue.append(start)
    while queue:
        point = queue.popleft()

        for i in range(1, 7):
            ni = point + i
            if 1 <= ni < 101 and mat[ni] > mat[point] + 1:
                if ladder[ni]:
                    if mat[ladder[ni][0]] > mat[point] + 1:
                        mat[ladder[ni][0]] = mat[point] + 1
                        queue.append(ladder[ni][0])
                elif baaaam[ni]:
                    if mat[baaaam[ni][0]] > mat[point] + 1:
                        mat[baaaam[ni][0]] = mat[point] + 1
                        queue.append(baaaam[ni][0])
                else:
                    mat[ni] = mat[point] + 1
                    queue.append(ni)



# 인풋
n, m = map(int, input().split())
ladder = [[] for _ in range(101)]
baaaam = [[] for _ in range(101)]
mat = [9999] * 101
for _ in range(n):
    ladder_start, ladder_end = map(int, input().split())
    ladder[ladder_start].append(ladder_end)

for _ in range(m):
    baaaam_start, baaaam_end = map(int, input().split())
    baaaam[baaaam_start].append(baaaam_end)
start = 1
end = 100


# 아웃풋
sol(start)
print(mat[100])
