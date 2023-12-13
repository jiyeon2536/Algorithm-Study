def solution(numbers, target):
    answer = 0
    # 완전탐색 문제
    # +, -를 사용해서 target넘버에 맞으면 answer ++
    mx = sum(numbers)
    def f(i, sv):
        nonlocal answer
        if i == len(numbers):
            if mx - 2 * sv == target:
                answer += 1
            return 
        f(i + 1, sv + numbers[i]) 
        f(i + 1, sv)
    f(0, 0)

    return answer
