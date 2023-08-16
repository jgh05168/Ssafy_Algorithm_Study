from collections import deque

def solution(priorities, location):
    answer = 0
    result = []
    deq = deque([[v,i] for i,v in enumerate(priorities)])
    
    while len(deq):
        x = deq.popleft()
        if deq and max(deq)[0] <= x[0]:
            result.append(x[1])
        else:
            if not deq:
                result.append(x[1])
                break
            deq.append(x)
    return result.index(location) + 1