N = int(input())
arr = list(map(int, input().split()))
cst = [-1] * (N+1)
#cst[0] = arr[0]  # 1장 사는 경우
arr.insert(0, 0)
cst[0] = 0 
# print(arr)
# 2장 사는 경우는 2장 짜리를 사는 경우와 1장을 2번 사는 경우
for i in range(1, N+1):
    for j in range(1, i+1):
        if cst[i] == -1:
            cst[i] = cst[i-j] + arr[j]  # dp에 값을 처음 넣는 경우
        else:
            cst[i] = min(cst[i-j] + arr[j], cst[i])  # 기존값과 갱신 값 비교
print(cst[N])
