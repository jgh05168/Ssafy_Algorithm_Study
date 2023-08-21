li = [list(map(int,input().split())) for _ in range(19)]
dx = [1,1,0,1]
dy = [0,1,1,-1]

res = 0
res_2 = []
for y in range(19):
    for x in range(19):
        if li[y][x] == 1:
            for i in range(4):
                for k in range(-2,3):
                    nx = x + dx[i]*k
                    ny = y + dy[i]*k

                    if 0<= nx <19 and 0<= ny <19 and li[ny][nx] == 1:
                        pass
                    else:
                        break
                    
                else:
                    for k in (3,-3):
                        nx = x + dx[i]*k
                        ny = y + dy[i]*k
                        
                        if 0<= nx <19 and 0<= ny <19 and li[ny][nx] == 1:
                            break
                    else:
                        res_2 = (y + dy[i]*-2+1,x + dx[i]*-2+1)
                        res = 1

        if li[y][x] == 2:
            for i in range(4):
                for k in range(-2,3):
                    nx = x + dx[i]*k
                    ny = y + dy[i]*k

                    if 0<= nx <19 and 0<= ny <19 and li[ny][nx] == 2:
                        pass
                    else:
                        break
                    
                else:
                    for k in (3,-3):
                        nx = x + dx[i]*k
                        ny = y + dy[i]*k
                        
                        if 0<= nx <19 and 0<= ny <19 and li[ny][nx] == 2:
                            break
                    else:
                        res_2 = (y + dy[i]*-2 +1,x + dx[i]*-2 +1)
                        res = 2
print(res)
print(*res_2)