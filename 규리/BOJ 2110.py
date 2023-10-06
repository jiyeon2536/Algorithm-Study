import sys
input = sys.stdin.readline

N, C = map(int, input().split())  # N:집 개수 / C:공유기 개수
x = [int(input()) for _ in range(N)]  # 집 좌표
x.sort()

start, end = 1, x[-1]-x[0]  # start:최소값 1, end:최대 거리

while start <= end:
    mid = (start + end) // 2
    idx, cnt = 0, 1  # 공유기 설치한 위치 인덱스, 공유기 설치 개수
    for i in range(1, N):
        # 앞에 설치한 위치와 현재 위치 사이의 거리가 mid 간격 이상이면 설치 & 설치 위치 인덱스 바꿔줌
        if x[i] - x[idx] >= mid:
            cnt += 1
            idx = i

    if cnt >= C:
        start = mid + 1
    else:
        end = mid - 1

print(end)
