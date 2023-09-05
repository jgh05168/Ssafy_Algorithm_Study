def track(a,b,c):
    global res
    if a > b:
        return
    elif a == b:
        if res > c:
            res = c
    else:
        track(2*a,b,c + 1)
        track(int(str(a)+'1'),b,c+1)
        
A, B = map(int,input().split())
res = 99999999999
track(A,B,1)
if res == 99999999999:
    print(-1)
else:
    print(res)
