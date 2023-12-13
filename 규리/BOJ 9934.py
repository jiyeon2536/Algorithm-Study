'''
4
8 4 9 2 10 5 11 1 12 6 13 3 7

1
2 3
4 5 6 7
8 9 10 11 12 13
'''

K = int(input())
nums = list(map(int, input().split()))
# i번째 줄의 노드 개수: 2**i
# (K-1)번째 줄(마지막 줄)의 노드 개수 y 구하기
N = 0
for i in range(K):
    N += 2**i
x = N - len(nums)
y = 2**(K-1) - x
answer = []

'''
8 4 9 2 10 5 11 1 12 6 13 3 7 -> [8, 9, 10, 11, 12, 13]
4 2 5 1 6 3 7 -> [4, 5, 6, 7]
2 1 3 -> [2, 3]
1 -> [1]

'''

while True:
    # K-1 부터 0 까지
    for i in range(K-1, -1, -1):
        lst = []
        for j in range(len(nums)):
            a = nums.pop(j)
            lst.append(a)
            # i번째 줄의 리스트 길이가 2**i 가 되면 break, i=K-1 일 때는 리스트 길이가 y가 되면 break
            if (i != K-1 and len(lst) == 2 ** i) or (i == K-1 and len(lst) == y):
                break
        answer.insert(0, lst)
    if len(nums) == 0:
        break

for ans in answer:
    print(*ans)
