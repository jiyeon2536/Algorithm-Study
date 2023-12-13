# 모음은 최소 1개 / 자음은 최소 2개
def check(string):
    result = False
    aeiou_cnt = 0

    # 문자열에서 모음의 개수를 카운팅
    for i in string:
        if i in aeiou:
            aeiou_cnt += 1

    # 모음의 수를 제외한 문자들, 즉 자음의 개수도 고려
    if aeiou_cnt > 0 and L - aeiou_cnt > 1:
        result = True

    return result


# 사전 순으로 이루어진 문자열 조합 생성
def comb(res, depth):
    if depth == C:
        # 길이가 L이고 조건에 충족하는 문자열 출력
        if len(res) == L and check(res):
            print(res)
        return

    comb(res + arr[depth], depth + 1)
    comb(res, depth + 1)


L, C = map(int, input().split())
arr = sorted(input().split())
# 모음을 모음 (아 ㅋㅋ)
aeiou = 'aeiou'
comb("", 0)
