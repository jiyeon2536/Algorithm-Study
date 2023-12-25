# 메뉴 리뉴얼
from itertools import combinations
def solution(orders, course):
    answer = []
    
    for num in course:
        # 개수마다 딕셔너리 초기화
        candidates = {}
        mx_value = 2
        for order in orders:
            comb = combinations(order, num)
            for c in comb:
                tmp = sorted(list(c))
                s = ''.join(tmp)
                if s in candidates:
                    candidates[s] += 1
                else:
                    candidates[s] = 1
                    
        for candidate in candidates:
            if candidates[candidate] >= mx_value:
                mx_value = candidates[candidate]
        
        for key in candidates:
            if candidates[key] == mx_value:
                answer.append(key)
        
        
    answer.sort()
    
    return answer