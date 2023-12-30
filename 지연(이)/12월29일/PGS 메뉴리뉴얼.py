from itertools import combinations

def solution(orders, course):
    
    def compare_two_string(str1,str2):
        s1 = set(str1)
        s2 = set(str2)
        s3 = s1 & s2
        return s3
    
    def count_all_case(order):
        cnt = 0
        for other_order in orders:
            other_order = set(other_order)
            intersection = order & other_order
            if intersection == order:
                cnt+=1
        return cnt


    
    answer_orderName = set()
    answer_cnt = []
    N = len(orders)
    
    # str1 str2 비교해서 공통된 문자들이 있는가
    for i in range(N-1):
        for j in range(i+1, N):
            s = compare_two_string(orders[i], orders[j])
            
            # 있다면 만들 수 있는 모든 조합
            # 각 조합이 orders에 몇번 포함되는지, 최빈값 찾아서 저장해야함
            # 겹치는 문자열은 pass해도 될 것 같은데, answer list가 아닌 set으로 변경?
            if len(s)>1:
                for num in course:
                    if len(s)<num:
                        continue
                    for order in combinations(s, num):
                        order_str = ''.join(sorted(list(order)))
                        if order_str not in answer_orderName:
                            cnt = count_all_case(set(order))
                            answer_orderName.add(order_str)
                            answer_cnt.append((cnt,order_str))
    
#   답을 어떻게 저장하지?
#  answer_cnt 에는 (횟수와 문자열)을 저장함. 그걸 sort함(횟수 큰 순으로, 문자열 길이가 긴 순으로)

#  아직 방문한 적 없으면 answer.append + visit
# 방문 했는데 최빈값이랑 동일한 횟수의 문자열이면, answer.append
    visit = [0]*11
    answer_cnt.sort(key=lambda x:(-x[0], -len(x[1])))
    answer = []
    # print(answer_cnt)
    for cnt, order in answer_cnt:
        if not visit[len(order)]:
            answer.append(order)
            visit[len(order)] = cnt
        elif visit[len(order)]==cnt:
            answer.append(order)
    
    answer.sort()
    return answer
