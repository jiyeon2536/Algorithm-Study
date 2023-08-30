import sys
from collections import deque
input = sys.stdin.readline

# 로프의 개수
N = int(input())

# 각 로프가 버틸 수 있는 최대 중량
rope = [int(input()) for _ in range(N)]
rope.sort()
rope = deque(rope)

result = []

while len(rope) > 1:
    # 최저 중량 * 전체 로프 개수 가 최대 하중 보다 크면
    if len(rope) > 1 and len(rope) * rope[0] > rope[-1]:
        result.append(len(rope) * rope[0])
        rope.popleft()
    else:
        if len(rope) == 1:
            result.append(rope[-1])
        else:
            rope.popleft()
if N == 1:
    print(rope[0])
else:
    print(max(result))

