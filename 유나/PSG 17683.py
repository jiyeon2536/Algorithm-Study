def solution(m, musicinfos):
    answer = '(None)'
    mx_time = 0
    
    # m의 악보 리스트 생성
    sheet_m = []
    for i in m:
        if i != '#':
            sheet_m.append(i)
        else:
            sheet_m[-1] += "#"
    length_m = len(sheet_m)
    
    # 방금그곡 리스트 순회하면서 찾기
    for info in musicinfos:
        music = info.split(',')
        sheet = []
        for i in music[-1]:
            if i != '#':
                sheet.append(i)
            else:
                sheet[-1] += "#"
        # 재생 시간 time : 종료시간에서 시작시간 빼기
        time = (int(music[1][:2]) * 60 + int(music[1][3:])) - (int(music[0][:2]) * 60 + int(music[0][3:]))
        # 재생된 음악 piece 생성
        length = len(sheet)
        piece = sheet * (time // length) + sheet[:time % length]
        
        # m이 piece에 포함되는 경우
        # print(sheet_m)
        # print(piece)
        for idx in range(time-length_m+1):
            # print(time-len(sheet_m))
            # print(piece[idx:idx+len(sheet_m)])
            # print(sheet_m)
            # print(piece[idx:idx+len(sheet_m)] == sheet_m)
            if piece[idx:idx+length_m] == sheet_m and time > mx_time:
                answer = music[2]
                mx_time = time
        
    return answer
