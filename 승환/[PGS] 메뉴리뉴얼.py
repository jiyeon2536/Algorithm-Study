from itertools import combinations, permutations
def solution(orders, course):
    answer = []
    def find(k, num):
        perm = list(combinations(k, num))
        for i in range(len(perm)):
            temp = "".join(sorted(perm[i]))
            # temp2 = (sorted(temp))
            # print(temp2)
            if temp in dic:
                dic[temp] += 1
            else:
                dic[temp] = 1
                
    # 최소 2명 이상의 손님에게서 주문된 구성만 코스요리에 들어간다
    # 결과값은 정렬해서 내보내야 한다
    # 종류의 개수가 같을 때, 가장 많이 주문된 메뉴를 넣는다.
    # 65 - 90
    # 조합 만들어서 딕셔너리에 추가, 값이 가장 높은 두개 출력
    for i in course:
        dic = {}
        for j in orders:
            find(j, i)
        d2 = sorted(dic.items(), key = lambda x: x[1])
        # print(d2)
        if d2:
            mx = d2[-1][1]
            for i in range(len(d2) - 1, 0, -1):
                if d2[i][1] == mx and d2[i][1] >= 2:
                    answer.append(d2[i][0])
    answer.sort()
    return answer
