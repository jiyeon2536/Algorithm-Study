N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
chi = []
hou = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            chi.append([i, j])  # 치킨집 리스트를 찾는다.
        elif arr[i][j] == 1:
            hou.append(([i, j]))  # 가정집 리스트를 찾는다.

# 치킨집 리스트에서 부분집합으로 M개를 뽑는다.
# M개의 치킨집에서 집 리스트와의 치킨 거리를 구하고, M개중 최솟값을
# 도시의 치킨 거리에 ++한다.
# M개의 부분집합 만큼 도시의 치킨 거리 모음리스트에 넣고, 그 중 최솟값을 출력한다.
### 크기가 M인 부분집합 gpt 썼음
### 크기가 M인 부분집합 구하는 연습하면 좋을듯
def generate_subsets(nums, M):
    def backtrack(start, subset):
        if len(subset) == M:
            subsets.append(subset[:])  # 새로운 부분집합 추가
            return
        for i in range(start, len(nums)):
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

    subsets = []
    backtrack(0, [])
    return subsets


subsets = generate_subsets(chi, M)
res = []  # 최종
while subsets:  # subsets : 크기가 M인 부분집합
    t = subsets.pop(0)
    res3 = []  # 최소인 부분집합의 합을 구할 배열
    for i in range(len(hou)):  # 집배열 길이만큼 돌려라
        res2 = []
        for j in range(len(t)):  # 치킨집 하나하나 반복문 돌면서 비교
            sv = 0
            sv += abs(hou[i][0] - t[j][0])  # x축 길이별 비교
            sv += abs(hou[i][1] - t[j][1])  # y축 길이별 비교
            res2.append(sv)  # 각 치킨집에서 집 까지의 치킨 거리 넣고
        res3.append(min(res2))  # 치킨거리 최솟값을 넣는다.
    res.append(sum(res3))  # 부분집합별 치킨 거리 최솟값의 합을 최종 비교에 넣고
print(min(res))  # 각 부분집합별 치킨 거리 합의 최솟값을 출력한다.

