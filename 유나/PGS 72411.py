def solution(orders, course):
    from itertools import combinations
    answer = []
    for num in course:
        # 종류를 받을 딕셔너리
        course_type = dict()
        # 코스 개수만큼 주문한 사람이 2명 이상인 경우
        if sum(map(lambda x: len(x) >= num, orders)) >= 2:
            for order in orders:
                combs = list(combinations(order, num))
                # num 개수에 맞는 조합 구하기
                for comb in combs:
                    # 정렬된 조합을 키로 생성하여 +1 해주기
                    course_type.setdefault(''.join(sorted(comb)), 0)
                    course_type[''.join(sorted(comb))] += 1
        # 주문 사람 많은 순으로 정렬
        res = sorted(course_type.items(), key = lambda x : x[1], reverse = True)
        # 주문한 사람이 2명 이상이고, 가장 많이 주문된 경우 answer에 추가
        for fin in res:
            if fin[1] == res[0][1] and res[0][1] >= 2:
                answer.append(fin[0])
    return sorted(answer)
