# 암호만들기

# 조합함수
# n : 전체 개수, r : 뽑을 개수, s: 시작인덱스
def ncr(n, r, s):
    # 더 이상 뽑지 않아도 된다면  tr과 new_s를 더하고 암호 정렬한 후 append
    if r == 0:
        res.append(''.join(sorted(tr + new_s)))
        return
    else:
        # 시작 인덱스부터 n-r+1까지
        for i in range(s, n - r + 1):
            # 이전에 추가되지 않은 값일때만 값을 입력
            if visited[i] == 0:
                new_s[r-1] = arr[i]
                ncr(n, r-1, i + 1)
                
import sys
input = sys.stdin.readline

# c개의 문자 중 4개로 암호 생성
l, c = map(int, input().strip().split())
arr = list(input().strip().split())

# 모음 인덱스를 받을 mo, 자음 인덱스를 받을 ja
# 이미 사용한 글자를 표현하기 위한 visitied 배열
# 결과를 받기 위한 res 리스트 생성
mo = []
ja = []
visited = [0] * c
res = []


# mo와 ja에 각각 모음, 자음에 해당하는 인덱스 입력
for i in range(len(arr)):
    # 아스키 코드로 비교하여 모음이라면 해당 인덱스를 mo에
    if ord(arr[i]) in [97, 101, 105, 111, 117]:
        mo.append(i)
    # 아니라면 ja에 append
    else:
        ja.append(i)

# 모음 1개, 자음 2개가 반드시 포함되어야 하므로
# 모음, 자음 리스트를 순회하면서 3개의 값을 미리 입력
for i in mo:
    # 반드시 자음 2개가 포함되어야 하므로 길이보다 하나 적게 순회
    for j in range(len(ja)-1):
        for k in range(j+1, len(ja)):
            # 추가 암호를 받을 new_s 생성
            new_s = [0] * (l-3)
            # 미리 선택할 암호를 받을 tr
            tr = [0] * 3
          
            # 입력될 인덱스에 대하여 방문 체크
            visited[i] = 1
            visited[ja[j]] = 1
            visited[ja[k]] = 1
          
            # tr에 입력
            tr[0] = arr[i]
            tr[1] = arr[ja[j]]
            tr[2] = arr[ja[k]]
          
            # ncr 진행
            ncr(c, l-3, 0)

            # 방문 체크열 복구
            visited[i] = 0
            visited[ja[j]] = 0
            visited[ja[k]] = 0

# 암호들을 사전식으로 정렬하여 출력
for item in sorted(list(set(res))):
    print(item)
  
