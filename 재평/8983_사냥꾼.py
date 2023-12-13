import sys
input = sys.stdin.readline

M, N, L = map(int, input().split())
# 사냥꾼이 있는 위치
hunter = list(map(int, input().split()))
target_coordinate = []
for i in range(N):
    a, b = map(int, input().split())
    target_coordinate.append((a, b))

# 잡을 수 있는 동물의 수
cnt = 0
hunter.sort()
for a, b in target_coordinate:
    start, end = 0, len(hunter)-1
    mid = 0
    while start < end:
        mid = (start+end)//2
        if hunter[mid] < a:
            start = mid + 1
        elif hunter[mid] > a:
            end = mid - 1
        else:
            start = mid
            break
    # 사냥 가능한 범위
    if abs(hunter[start]-a)+b <= L:
        cnt += 1
    # 왼쪽
    elif start+1 < len(hunter) and abs(hunter[start+1]-a)+b <= L:
        cnt += 1
    # 오른쪽
    elif start > 0 and abs(hunter[start-1]-a)+b <= L:
        cnt += 1
print(cnt)