def hanoi(N,start,move):
    if N == 1:
        print(li[1], move)
        li[1] = move
        return
    else:
        if move == 3:
            if start == 1:
                hanoi(N-1,1,2)
                print(li[N], move)
                li[N] = move
                hanoi(N-1,2,3)
            if start == 2:
                hanoi(N-1,2,1)
                print(li[N], move)
                li[N] = move
                hanoi(N-1,1,3)
        if move == 2:
            if start == 1:
                hanoi(N-1,1,3)
                print(li[N], move)
                li[N] = move
                hanoi(N-1,3,2)
            if start == 3:
                hanoi(N-1,3,1)
                print(li[N], move)
                li[N] = move
                hanoi(N-1,1,2)
        if move == 1:
            if start ==2:
                hanoi(N-1,2,3)
                print(li[N], move)
                li[N] = move
                hanoi(N-1,3,1)
            if start ==3:
                hanoi(N-1,3,2)
                print(li[N], move)
                li[N] = move
                hanoi(N-1,2,1)


N = int(input())
li = [0]*(N+1)
li[1] = 1
for i in range(2,N+1):
    li[i] = 2*li[i-1] + 1
print(li[N])


li = [1]*(N+1)
if N <= 20:
    hanoi(N,1,3)