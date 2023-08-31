N = int(input())
arr = [[]]
for i in range(N):
    x, y = map(int, input().split())
    arr.append([x, y])
arr.sort()
vlg = [0] * N
oil = [0] * N
for j in range(1, N+1):
    vlg[j-1] = arr[j][0]
    oil[j-1] = arr[j][1]
p, l = map(int, input().split())
vlg.append(p)  # 여기까지 오름차순으로 마을거리, 오일을 정렬하고 1차원 배열에 담았음
cur = l  # 시작 기름
i = 0  # 움직이는 범위
oil_lst = []
res = 0
while True:
    if cur >= vlg[-1]:  # 도착점을 넘어갈 만큼 기름을 모은다면
        break
    if cur >= vlg[i]:  # 갈 수 있는 마을 위치
        oil_lst.append(oil[i])  # 갈 수 있었던 오일 추가
        i += 1
        continue
    else:  # 현재 기름으로 못가는 경우
        if oil_lst:
            while oil_lst:  # 갈 수 있었던 곳이 있다면
                if cur >= vlg[i]:  # 만약 현재 기름이 마을 통과한다면 
                    break
                else:
                    oil_lst.sort()  # 정렬해서
                    cur += oil_lst.pop()  # 최댓값을 뽑아서 더한다.
                    res += 1  # 마을 들렸으니까 ++
        else:  # 들릴 마을이 없다면 -1
            res = -1
            break
print(res)
