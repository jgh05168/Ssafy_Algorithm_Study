dx = [0,-1,-1,0,1,1,1,0,-1]
dy = [0,0,-1,-1,-1,0,1,1,1]

dx2 = [1,-1,-1,1]
dy2 = [1,1,-1,-1]

N,M = map(int,input().split())
li = [list(map(int,input().split())) for i in range(N)]

water = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

for i in range(M):
    d,s = map(int,input().split())
    # 이동
    move_water = []
    for y,x in water:
        nx = (x + dx[d]*s) % N
        ny = (y + dy[d]*s) % N
        
        li[ny][nx] += 1
        move_water.append((ny,nx))

    for y,x in move_water:
        plus = 0
        for k in range(4):
            nx2 = x + dx2[k]
            ny2 = y + dy2[k]

            if 0<=nx2<N and 0<=ny2<N and li[ny2][nx2]>=1:
                plus += 1
        li[y][x] += plus

    water = []
    for y in range(N):
        for x in range(N):
            if li[y][x] >=2 and (y,x) not in move_water:
                li[y][x] -=2
                water.append((y,x))
sum_ = 0
for y in range(N):
    for x in range(N):
        sum_ += li[y][x]

print(sum_)
        

            
