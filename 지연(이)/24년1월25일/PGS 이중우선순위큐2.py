import heapq
def solution(operations):
    lst = []
    for command in operations:
        command = list(command.split())
        if command[0] == 'I':
            lst.append(int(command[1]))
            lst.sort()
        else:
            if not lst:
                continue
            if command[1] == '-1':
                lst.pop(0)
            else:
                lst.pop()

    if not lst:
        return [0,0]
    elif len(lst)==1:
        return [lst[0], lst[0]]
    return [lst.pop(),lst.pop(0)]
