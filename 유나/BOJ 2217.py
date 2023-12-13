# 로프 개수 입력
n = int(sys.stdin.readline())
# 각 로프가 견딜 수 있는 중량 입력
weight = [int(sys.stdin.readline()) for _ in range(n)]

# 중량 정렬
weight.sort()

# 최댓값 생성
mx = 0

# 개수만큼 순회하면서
for i in range(n):
    # 최댓값 갱신
    # 무게 * 개수 : 0부터 순차적으로 최솟값 * 남은 로프의 개수
    mx = max(weight[i] * (n - i), mx)

print(mx)
