def solution(numbers, target):
    N = len(numbers)
    answer = 0
    arr = [0]*N
    
    def calc(i, num):
        nonlocal arr, answer
        if i == N:
            if num == target:
                answer += 1
            return
        
        arr[i] = 1  # 1:빼기, 0:더하기
        calc(i+1, num - 2*numbers[i])
        arr[i] = 0
        calc(i+1, num)
        
    calc(0, sum(numbers))
    
    return answer
