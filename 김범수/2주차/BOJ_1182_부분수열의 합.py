N,S = map(int,input().split())
li = list(map(int,input().split()))
res = 0
for i in range(1<<N):
    subset =[]
    for j in range(N):
        if i & (1<<j):
            subset.append(li[j])
    if subset and sum(subset) == S:
        res +=1
print(res)