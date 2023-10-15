# 트리의 원소(노드)
class node:
    def __init__(self, data):
        # 노드의 번호
        self.data = data
        # 노드의 자식 노드들
        self.next = [None, None]

# 트리
class tree:
    def __init__(self):
        # 트리의 루트
        self.root = None

# 후위 선회
def postorder(vertex: node):
    if vertex.next[0]:
        postorder(vertex.next[0])

    if vertex.next[1]:
        postorder(vertex.next[1])

    print(vertex.data)

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

# 트리 생성!
trees = tree()
# 방금 만든 트리의 루트는 첫 번째 입력
trees.root = node(int(input().strip()))

# 입력이 주어질 때까지...
try:
    while True:
        num = int(input().strip())
        # 트리의 루트에서부터 자리를 찾아가기 위해
        # 처음 탐색 지점을 루트로 지정
        now_node = trees.root

        while True:
            # 왼쪽 자식 노드 방향
            next_idx = 0

            # 현재 노드보다 값이 크다면 오른쪽 자식 노드 방향을 보게 함
            if now_node.data < num:
                next_idx = 1

            # 만약 그 방향에 자식 노드가 없다면 그 자리에 노드를 추가
            if now_node.next[next_idx] == None:
                now_node.next[next_idx] = node(num)
                break
            # 그 방향에 자식 노드가 있다면 그 노드가 다음 탐색 노드가 됨
            else:
                now_node = now_node.next[next_idx]
# 입출력 에러에 대해서만 작동
except EOFError:
    postorder(trees.root)
