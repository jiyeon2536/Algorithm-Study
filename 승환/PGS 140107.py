def solution(k, d):
    answer = 0
    for i in range(0, d + 1, k):
        answer += (d * d - i * i) ** 0.5 // k + 1
    return answer
