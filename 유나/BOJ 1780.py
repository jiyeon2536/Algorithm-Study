'''
1. 종이가 모두 같은 수라면 그대로 사용
2. (1)이 아닌 경우, 9등분하여 (1) 과정 반복
'''
import sys
input = sys.stdin.readline

# 2번 : 9등분으로 자르기
def divide(n, arr):
    # 가로, 세로 3등분씩
    s = n // 3
    # 순회하면서 new 리스트 생성
    for i in range(0, n, s):
        for j in range(0, n, s):
            new = []
            for k in range(s):
                new.append(arr[i + k][j:j + s])
            check(s, new)

# 1번 조건에 충족하는지 체크
def check(n, arr):
    global cnt_minus, cnt_0, cnt_1
    cnt = 0 # 모두 같은지 확인하기 위한 카운트
    num = arr[0][0] # 첫번째 원소

    for i in range(n):
        for j in range(n):
            # 첫번째 원소와 동일하면 cnt +1
            if arr[i][j] == num:
                cnt += 1
            # 조건 만족하지 않으면, divide에 넘기고 return
            else:
                divide(n, arr)
                return
    # 개수가 맞으면 더해줘용
    if cnt == n ** 2:
        if num == -1:
            cnt_minus += 1
        elif num == 0:
            cnt_0 += 1
        else:
            cnt_1 += 1


n = int(input().strip())
arr = [list(map(int, input().strip().split())) for _ in range(n)]
cnt_minus = cnt_0 = cnt_1 = 0
check(n, arr)

print(cnt_minus)
print(cnt_0)
print(cnt_1)
