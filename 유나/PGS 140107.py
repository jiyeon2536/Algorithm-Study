def solution(k, d):
    answer = 0
    import math
    # d^2 = x^2 + y^2
    # x^2 = d^2 - y^2
    # 0 ~ d 까지 k 간격으로
    for y in range(0, d+1, k):
        # k 간격으로 나눈 몫 + 0
        answer += math.sqrt(d**2-y**2) // k + 1
    return answer
