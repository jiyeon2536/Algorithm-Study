def solution(targets):
    answer = 0
    
    # e, s를 기준으로 정렬
    targets.sort(key = lambda x: [x[1], x[0]])
    
    e = 0
    # e가 s보다 큰 경우 한번에 포격 가능
    # e가 s보다 작거나 같은 경우에는 포격 +1, e값 갱신
    for cord in targets:
        if e <= cord[0]:
            answer += 1
            e = cord[1]
    return answer
