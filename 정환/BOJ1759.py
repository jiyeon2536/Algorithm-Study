import itertools
import sys
from itertools import combinations
input = sys.stdin.readline

L, C = map(int, input().split())

arr = input().split()

# 문자들의 리스트를 먼저 사전순으로 정렬
arr.sort()
# 조합 함수를 이용하여 길이가 L 인 각 문자들이 이루는 조합을 생성
a = combinations(arr, L)

ans = []
# 만들어진 조합을 순회하면서 조건 탐색
for i in a:
    gather_count = 0
    gather_count += i.count('a')
    gather_count += i.count('e')
    gather_count += i.count('i')
    gather_count += i.count('o')
    gather_count += i.count('u')
    # 조건은 모음이 최소 1개 자음이 최소 2개 이상으로 구성되어야 한다.
    # 그렇지 않은 조합들은 전부 패스
    if gather_count == 0 or gather_count > L - 2:
        continue
    # 조건을 충족한다면 출력
    else:
        print(''.join(i))
