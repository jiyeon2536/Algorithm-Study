import sys
input = sys.stdin.readline

def findMX():
    # 최댓값을 찾을 때 다음 숫자를 입력할 위치 뒤의 '<' 부등호의 개수
    cnt_mx = 0
    i = 0
    while i != len(arr):
        # 최대 수를 만들어야 하므로 '>' 의 왼쪽엔 올 수 있는 수 중 가장 큰 수가 와야함
        if arr[i] == '>':
            # 고려해야 할 '<' 부동흐의 개수가 0이므로 남은 수 중 가장 큰 수를 추가
            if cnt_mx == 0:
                mx.append(numb_mx.pop())
                i += 1
            while cnt_mx != 0:
                # 남은 숫자들 중 큰 순서부터 '<' 부등호의 개수만큼 남겨둔 다음 숫자를 추가
                mx.append(numb_mx.pop(- cnt_mx - 1))
                cnt_mx -= 1

        elif arr[i] == '<':
            cnt_mx += 1
            i += 1
    # 순회를 종료할 때 까지 '>' 부등호로 마무리 되지 않는 경우도 있으므로
    while True:
        if cnt_mx == 0:
            mx.append(numb_mx[-1])
            break
        mx.append(numb_mx.pop(- cnt_mx - 1))
        cnt_mx -= 1

    return mx


def findMN():
    cnt_mn = 0
    j = 0
    while j != len(arr):
        if arr[j] == '<':
            if cnt_mn == 0:
                mn.append(numb_mn.pop(0))
                j += 1
            while cnt_mn != 0:
                mn.append(numb_mn.pop(0 + cnt_mn))
                cnt_mn -= 1
        elif arr[j] == '>':
            cnt_mn += 1
            j += 1
    while True:
        if cnt_mn == 0:
            mn.append(numb_mn.pop(0))
            break
        mn.append(numb_mn.pop(0 + cnt_mn))
        cnt_mn -= 1

    return mn

# 부등호 문자 개수
k = int(input())

arr = list(input().split())

# 0 ~ 9 숫자는 한 번씩만 사용가능
numb_mx = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
numb_mn = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

mx = []
mn = []

findMX()
findMN()

mx = ''.join(mx)
mn = ''.join(mn)

print(mx)
print(mn)


