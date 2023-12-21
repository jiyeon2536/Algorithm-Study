# 오른쪽으로 이동하는게 좋을지
# JJJJAAA
# 왼쪽으로 이동하는게 좋을지
# AAAAJJJ
# 오른쪽으로 이동하다가, 왼쪽으로 이동하는게 좋을지
# JAAAAAJ

# JJAAAJJ
# J1 왼 J2 오오 J4 오 J3
# JJJAJJJ
# J1 J2 J3 J4 J5 J6 오른쪽으로 쭉 이동
# 현위치에서 가장 가까운거?
# JAJAAAAJ
# J1 J3 J2 4 / J1 J2 J3 5
# JAAJJAAJJ
# 왼쪽으로 쭉 이동 6

# 완전 탐색? index int list
# permutation
# now, nxt
# count = min(count)

# 왼쪽에서 더 가까운 애들, 오른쪽에서 더 가까운 애들
# 근데 왔던 곳으로 안가는게 더 좋을거임
# alphabet char list / index int list

from itertools import permutations
def solution(name):
    index = []
    for i in range(len(name)):
        if name[i]!='A':
            index.append(i)
    
    move_cnt = float('inf')
    indexs = permutations(index, len(index))
    for index in indexs:
        cnt = 0
        now = 0
        for i in range(len(index)):
            nxt = index[i]
            # if abs(nxt-now)<=abs(now+len(name)-nxt):
            #     cnt+=abs(nxt-now)
            # else:
            #     cnt+=abs(now+len(name)-nxt)
            if now<=nxt:
                if nxt-now <= now + len(name)-nxt:
                    cnt+=nxt-now
                else:
                    cnt+=(now + len(name) - nxt)
            else:
                if now-nxt <= nxt + len(name) - now:
                    cnt+=now-nxt
                else:
                    cnt+=(nxt+len(name)-now)
            now = nxt
        move_cnt = min(move_cnt, cnt)

    alpha_cnt = 0
    for alpha in name:
        if alpha=="A":
            continue
        elif ord(alpha)-ord('A')<ord('Z')-ord(alpha)+1:
            alpha_cnt += ord(alpha)-ord('A')
        else:
            alpha_cnt += ord('Z')-ord(alpha)+1
    return alpha_cnt + move_cnt
