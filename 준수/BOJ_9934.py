def order(idx, k):
    if k >= 0:
        # 높은 층부터 0번째 인덱스에 해당하는 res 배열에 담기
        res[K - k - 1].append(arr[idx])
        # 자식 노드의 위치는 트리의 높이에 따라 일정한 비율을 가짐
        # 층을 하나씩 내려가면서 => k를 1씩 감소시키면서
        order(idx - 2 ** (k - 1), k - 1)
        order(idx + 2 ** (k - 1), k - 1)

K = int(input())
# 인덱스를 1번부터 사용하기 위해 앞에 [0] 추가
arr = [0] + list(map(int, input().split()))
res = [[] for _ in range(K)]
# 완전이진트리의 경우에 부모 노드 인덱스는 일정
order((2 ** K) // 2, K - 1)
for line in res:
    print(*line)