import sys
input = sys.stdin.readline

N = int(input())  # 로프개수
lst = [int(input()) for _ in range(N)]  # 각 로프의 최대 중량
lst.sort(reverse=True)

# (로프 무게) * (최대중량이 같거나 무거운 로프 개수)
ans = [(lst[i] * (i+1)) for i in range(N)]
ans.sort(reverse=True)

result = ans[0]
print(result)
