A, B = map(int, input().split())

def cut(B):
    B = B // 2
    return B

def popOne(B):
    B = str(B)
    B = B[:-1]
    if B == '':
        return
    else:
        return int(B)

cnt = 1

# 2를 곱하는 행동과 1을 수의 가장 오른쪽에 추가하는 행동을 역으로 실행
while True:
    # A 와 B 가 같아지면 종료
    if B == A:
        print(cnt)
        break
    # 만약 B 가 비어있다면 더 이상 만들 방법이 없기 때문에 -1 을 출력하고 종료
    if B == None:
        print(-1)
        break
    # B 가 짝수라면 B 에서 2를 나눈다
    if B % 2 == 0:
        B = cut(B)
    # B 의 맨 뒤 값이 '1' 이라면 1을 제거
    elif str(B)[-1] == '1':
        # 만약 B 가 비어있다면 더 이상 만들 방법이 없기 때문에 -1 을 출력하고 종료
        if B == '':
            print(-1)
            break
        B = popOne(B)
    # B 가 짝수인 상황과 맨 뒤의 값이 '1' 인 상황 외에는
    # 두 수를 정수 A 를 B로 바꿀 수 없기 때문에 -1 을 출력하고 종료
    else:
        print(-1)
        break
    # cut()과 popOne() 이 이루어지는 횟수만큼 더한 값이 필요한 연산의 최솟값
    cnt += 1