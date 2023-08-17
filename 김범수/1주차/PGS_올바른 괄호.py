def solution(s):
    
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
            print(stack)
        else:
            if len(stack) > 0 and stack[-1] =='(':
                stack.pop()
                print(stack)
            else:
                return False
    else:
        if stack == []:
            return True
        else:
            return False

print(solution('(())()'))
print()
print(solution('(()()'))

