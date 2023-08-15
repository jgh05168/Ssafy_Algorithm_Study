N = int(input())
li = list(input())
stack = []
dict = {}
# 숫자로 바꿔주기
#ABC*+DE/-
for i in li:
    if not i in ['*','+','-','/'] and not i in dict:
        dict[i] = float(input())
print(dict)
# 연산
for i in li:
    #피연산자 들일때, 스택에 넣기
    if not i in ['*','+','-','/']:
        stack.append(dict[i])
        print(stack)
    else:
       #아닐때는 뒤에서 부터 꺼내오기 순서 중요 
        b = stack.pop()
        a = stack.pop()
        if i == '*':
            stack.append(a * b)
        if i == '+':
            stack.append(a + b)
        if i == '-':
            stack.append(a - b)
        if i == '/':
            stack.append(a / b)
        print(stack)

print(f'{stack[0]:.2f}')
'''
5
ABC*+DE/-
1
2
3
4
5
'''

