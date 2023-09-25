n, m = map(int, input().split())  # n = 카드의 개수, m = 카드 합체를 몇 번 하는지
arr = list(map(int, input().split()))
# x번 카드와 y번 카드를 골라 그 두장에 쓰여진 수를 더한 값을 계산 한다.
# 계산한 값을 x번 카드와 y번 카드 두장 모두에 덮어 쓴다.
for i in range(m):
    arr.sort()
    s = arr[0] + arr[1]
    arr[0] = s
    arr[1] = s
print(sum(arr))
