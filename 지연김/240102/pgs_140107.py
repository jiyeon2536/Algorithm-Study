# 점 찍기
from math import sqrt
def solution(k, d):
    
    answer = 0
    lim = d**2
    for x in range(0, d+1, k):
        y = sqrt(lim - x**2)
        cnt = (y // k) + 1
        answer += cnt
        
    return answer