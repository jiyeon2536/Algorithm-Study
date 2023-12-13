def solution(phone_book):
    answer = True
    
    N = len(phone_book)
    phone_book.sort()
    phone = phone_book[0]
    
    for i in range(1, N):
        length = len(phone)
        if phone_book[i][:length] == phone:
            answer = False
        phone = phone_book[i]
    
    return answer
