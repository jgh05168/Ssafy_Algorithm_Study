# N과 M
N,M = map(int,input().split())
li = [i for i in range(1,N+1)]
res_li = []

for i in range(1<<N):
    res = ''
    for j in range(N):
        if i & (1<<j):
            res = res + str(li[j])
    
    if len(res) == M:
        res_li.append(res)

res_li = sorted(res_li)
for i in range(len(res_li)):
    for j in res_li[i]:
        print(j,end =" ")
    print()

