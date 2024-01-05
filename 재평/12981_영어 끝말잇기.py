def solution(n, words):
    i = 1
    prev_word = False
    used_words = []
    answer = False
    for word in words:
        if prev_word and word[0] != prev_word[-1] or word in used_words:
            if i%n:
                person = i%n
                turn = i//n + 1
            else:
                person = n
                turn = i//n
            return [person, turn]
        i += 1
        prev_word = word
        used_words.append(prev_word)
    return [0, 0]

# n = 3
# words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
