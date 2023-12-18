def solution(storey):
    answer = 0
    while storey:
        tmp = storey%10
        if tmp<5 or (tmp==5 and storey<10) or (tmp==5 and storey%100//10<5):
            answer += tmp
        else:
            storey += (10-tmp)
            answer += 10-tmp
        storey//=10
    return answer

print(solution(100000000))
# 1
print(solution(99999999))
# 2
print(solution(5656))
# 16
print(solution(26262))
# 16
print(solution(95))
# 6
print(solution(85))
# 7
print(solution(55))
# 10
print(solution(25))
# 7
print(solution(545))
# 14
print(solution(155))
# 11
print(solution(154))
# 10
print(solution(555))
# 14
