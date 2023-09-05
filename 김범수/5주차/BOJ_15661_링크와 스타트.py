def perm(subset):
    n = len(subset)
    sum_ = 0
    for i in range(n-1):
        for j in range(i+1,n):
            sum_ += li[subset[i]][subset[j]]
            sum_ += li[subset[j]][subset[i]]
        
    return sum_


N = int(input())
li = [list(map(int,input().split())) for _ in range(N)]
min_v = 100000000000

for i in range(1,1<<(N-1)):
    ss1 = []
    ss2 = []
    for j in range(N):
        if i & (1<<j):
            ss1.append(j)
        else:
            ss2.append(j)
    
    # 시작
    if len(ss1) >= 1 and len(ss2) >= 1:
        sng1 = perm(ss1)
        sng2 = perm(ss2)
        
        if min_v > abs(sng1 - sng2):
            min_v = abs(sng1 - sng2)
    
print(min_v)

