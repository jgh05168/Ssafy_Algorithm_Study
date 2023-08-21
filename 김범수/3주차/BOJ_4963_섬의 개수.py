while True:
    w, h = map(int,input().split())
    if w == 0 and h == 0:
        break
    li = [list(map(int,input().split())) for _ in range(h)]

    dx = [1,1,0,-1,-1,-1,0,1]
    dy = [0,1,1,1,0,-1,-1,-1]
    res = 0
    stack = []
    for y in range(h):
        for x in range(w):
            if li[y][x] == 1:
                res +=1
                stack.append((x,y))

                while stack:
                    x1 , y1 =stack.pop()
                    li[y1][x1] = 0
                    for i in range(8):
                        nx = x1 + dx[i]
                        ny = y1 + dy[i]
                        if 0<= nx <w and 0<= ny<h and li[ny][nx]==1 and not (nx,ny) in stack:
                            stack.append((nx,ny))
    print(res)
