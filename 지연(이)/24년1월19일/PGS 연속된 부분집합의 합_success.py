def solution(sequence, k):
    N = len(sequence)
    start = end = 0
    s = sequence[start]  # sum(sequenc[start:end+1])
    answer = [N, N + N]
    while start <= end and end < N:
        if s == k:
            # 값 갱신
            if end - start < answer[1] - answer[0]:
                answer = [start, end]
            elif end - start == answer[1] - answer[0]:
                if start < answer[0]:
                    answer = [start, end]
            s -= sequence[start]
            start += 1

        elif s < k:
            # 추가
            end += 1
            if end<N:
                s += sequence[end]
            else:
                break
        else:
            # 제거
            s -= sequence[start]
            start += 1

    return answer


