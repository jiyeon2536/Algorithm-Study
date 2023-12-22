import math


# 문자열 변경
def change_str(m):
    shap = {"C#": "X", "D#": "Y", "F#": "Z", "G#": "W", "A#": "V", "E#":"N"}
    tmp = ""
    for i in range(len(m)):
        if i + 1 < len(m) and m[i + 1] == '#':
            tmp += shap[m[i] + m[i + 1]]
        else:
            if m[i] == '#':
                continue
            tmp += m[i]
    return tmp


# 보이어 무어 알고리즘 m과 music 멜로디 비교
def find(str, ch):
    for i in range(len(str) - 2, -1, -1):
        if str[i] == ch:
            return len(str) - i - 1
    return len(str)


# str2에 str1이 있는지 없는지
def boyer_moore(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    i = 0
    while i <= len2 - len1:
        j = len1 - 1
        while j >= 0:
            if str1[j] != str2[i + j]:
                move = find(str1, str2[i + len1 - 1])
                break
            j -= 1
        if j == -1:
            return True
        else:
            i += move
    return False


def solution(m, musicinfos):
    answer = [("(None)", -1, 1439)]
    m = change_str(m)

    for music in musicinfos:
        music = music.split(",")
        start = list(map(int, music[0].split(":")))
        end = list(map(int, music[1].split(":")))

        # time -> min
        # start
        music[0] = start[0] * 60 + start[1]

        # playtime
        music[1] = (end[0] * 60 + end[1]) - music[0]

        # melody change
        # 1. change
        music[3] = change_str(music[3])
        # 2. playtime만큼 연장하기
        if len(music[3]) < music[1]:
            music[3] = music[3] * math.ceil(music[1] / len(music[3]))
        # 3. playtime만큼 자르기
        if len(music[3]) > music[1]:
            music[3] = music[3][:music[1]]

        # answer
        if boyer_moore(m, music[3]):
            answer.append((music[2], music[1], music[0]))

    answer.sort(key=lambda x: (-x[1], x[2]))
    # print(answer)
    return answer[0][0]


# print(solution("C", ["13:00,13:01,WORLD,F"]))
# print(boyer_moore("ABC", "BCABC"))
