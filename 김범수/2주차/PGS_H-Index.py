def solution(citations):
    li = sorted(citations,reverse = True)
    max_ = 0
    for i,x in enumerate(li):
        if x >= (i+1):
            max_ = i+1
    
    return max_
[6,4,4,4,4,4,4,4]