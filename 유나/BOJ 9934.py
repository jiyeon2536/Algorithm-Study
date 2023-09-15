# p : 노드 번호 i : 입력 순서
# 자식노드를 찾아가는 과정이 곱셈으로 이루어지기 때문에 초기값을 1로 지정
def graphs(p):
    global i
    # 전체 개수보다 작거나 같은 경우에만 순회
    if p <= n:
        graphs(p*2) # 왼쪽 노드
        # 입력 순서대로 트리 위치를 찾아 저장
        # p-1번 노드에 i번째 입력된 값
        i += 1
        tree[p-1] = arr[i]
        graphs(p * 2 + 1) # 오른쪽 노드

import sys
input = sys.stdin.readline

# 깊이 및 탐색 순서 받기
k = int(input().strip())
arr = list(map(int, input().strip().split()))

# 트리 노드 개수 받기
n = len(arr)

# 루트 노트부터 순서대로 받기위해 배열 생성
tree = [0] * n
i = -1 # 0부터 시작해주기 위해서

graphs(1)

s = 0
# 층별로 2의 승수만큼 노드를 가짐
for d in range(k+1):
    for j in range(2**d):
        if s+j < n: # 오른쪽 노드가 없는 경우를 대비
            print(tree[s+j], end = ' ')
    s += 2**d
    print()
