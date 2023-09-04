import sys
import itertools
input = sys.stdin.readline
cnt = 0

while True:
    cnt += 1

    arr = list(map(int, input().split()))
    if arr == [0]:
        break
    # 주어진 번호들의 개수 뽑기
    k = arr.pop(0)
    # 번호들만 남았음
    arr.sort()

    # 슈퍼 울트라 콤비네이션 파워 함수
    cmb = itertools.combinations(arr, 6)
    for i in cmb:
        print(*i)
    print()
