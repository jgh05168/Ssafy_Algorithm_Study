N = int(input())
li = list(input())
stack = []
dict = {}
for i in li:
    if not i in ['*','+','-','/'] and not i in dict:
        dict[i] = float(input())

for i in li:
    if not i in ['*','+','-','/']:
        stack.append(dict[i])
    else:
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
        

print(f'{stack[0]:.2f}')

