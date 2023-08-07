def solution(s):
    
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) > 0 and stack[-1] =='(':
                stack.pop()
            else:
                return False
    else:
        if stack == []:
            return True
        else:
            return False

