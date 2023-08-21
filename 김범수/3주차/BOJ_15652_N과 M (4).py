def backtrack(i,M,res):
    if i == M:
        print(*res)
        return
    else:
        for j in range(N):
            if not i or (i and res[-1]<=li[j]):
                res.append(li[j])
                backtrack(i+1,M,res)
                res.pop()

    


N, M = map(int,input().split())
li = [i for i in range(1,N+1)]
backtrack(0,M,[])