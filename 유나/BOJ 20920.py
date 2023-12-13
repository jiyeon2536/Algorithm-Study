import sys
n, m = map(int, sys.stdin.readline().strip().split())

# 딕셔너리 생성
my_dict = {}

for _ in range(n):
    text = sys.stdin.readline().strip()
    # 해당 키 값이 존재하지 않으면 키 생성 및 0값 입력
    my_dict.setdefault(text, 0)
    # 키 존재 여부 상관 없이, 해당 키가 나온다면 카운트 +1
    my_dict[text] += 1

# 값을 기준으로 정렬
my_dict = dict(sorted(my_dict.items(), key = lambda x : (-x[1], -len(x[0]), x[0])))
# 오름차순, 내림차순을 맞추기 어려운 경우에는 음수를 활용하는 것이 유용
# -x[1] : 빈출일 수록
# -len(x[1]) : 단어의 길이가 길 수록
# x[0] : 알파벳 순
for key, val in my_dict.items():
    if len(key) >= m:
        print(key)
