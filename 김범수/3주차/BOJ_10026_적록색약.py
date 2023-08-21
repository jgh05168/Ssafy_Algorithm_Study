import copy
N = int(input())
li = [list(input()) for _ in range(N)]
li2 = copy.deepcopy(li)

res = 0
res2 = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

stack = []
for y in range(N):
    for x in range(N):
        if li[y][x] in 'RGB':
            color = li[y][x]
            stack.append((x,y))
            res +=1
            while stack:
                x1,y1 = stack.pop()
                li[y1][x1] = 'v'
                for i in range(4):
                    nx = x1 + dx[i]
                    ny = y1 + dy[i]
                    if 0<=nx<N and 0<=ny<N and li[ny][nx] == color and not (nx,ny) in stack:
                        stack.append((nx,ny))
for y in range(N):
    for x in range(N):
        if li2[y][x] == 'G':
            li2[y][x] = 'R'

for y in range(N):
    for x in range(N):
        if li2[y][x] in 'RGB':
            color = li2[y][x]
            stack.append((x,y))
            res2 +=1
            while stack:
                x1,y1 = stack.pop()
                li2[y1][x1] = 'v'
                for i in range(4):
                    nx = x1 + dx[i]
                    ny = y1 + dy[i]
                    if 0<=nx<N and 0<=ny<N and li2[ny][nx] == color and not (nx,ny) in stack:
                        stack.append((nx,ny))

print(res, res2)

