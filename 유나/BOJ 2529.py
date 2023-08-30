# 순열 함수 생성
def perm(i, k):
    global arr, mx, mn
    # 기저 조건 : 최대 깊이에 도달했을 때
    if i == k:
        # 조건에 만족한 경우 추가
        total = []
        condition = True # 조건을 만족하는지?
        # 부등호 개수 만큼 순회
        for j in range(len(arr)):
            # 부등호가 > 일 때, 다음 값이 해당 값보다 작다면
            if arr[j] == '>' and p[j] > p[j + 1]:
                pass
            # 부등호가 < 일 때, 다음 값이 해당 값보다 크다면
            elif arr[j] == '<' and p[j] < p[j + 1]:
                pass
            # 만족하지 않는다면 조건 불만족
            else:
                condition = False
                break
        # 조건을 만족한다면 total 추가
        if condition:
            total.append(''.join(map(str, p)))

        # 만족하는 숫자조합을 지나가면서 최댓값, 최솟값 갱신
        for k in total:
            if int(mx) < int(k):
                mx = k
            if int(mn) > int(k):
                mn = k
        return
    # 유지 조건 : 사용한 열 체크 하면서 순열 조합 생성
    else:
        for j in range(10):
            # 방문한 적 없는 숫자라면
            if used[j] == 0:
                # 방문 체크
                used[j] = 1
                # 해당 깊이(인덱스) 값 입력
                p[i] = j
                # 재귀 함수
                perm(i + 1, k)
                # 방문체크 복구구
               used[j] = 0

import sys

n = int(sys.stdin.readline())   # 부등호의 개수
arr = sys.stdin.readline().split() # 부등호
used = [0] * 10 # 0~9까지 사용 여부 체크
p = [0] * (n + 1) # 부등호 + 1 만큼 숫자 필요
perm_list = [] # 숫자 조합 받을 리스트 생성
mx = 0
mn = 100000000000

perm(0, n + 1)

print(mx)
print(mn)
