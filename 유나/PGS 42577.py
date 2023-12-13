def solution(phone_book):
    answer = True
    # 정렬
    phone_book.sort()
    for idx in range(len(phone_book)-1):
        # 해당 번호가 다음 번호에 접두사인지 확인
        if phone_book[idx] == phone_book[idx+1][:len(phone_book[idx])]:
            answer = False
    return answer
