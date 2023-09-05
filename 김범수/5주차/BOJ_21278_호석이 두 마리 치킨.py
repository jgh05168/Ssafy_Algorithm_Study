from collections import deque

def dfs(a,b,k):
    visited = [0]*(N+1)
    visited[k] = 1
    q = deque([k])
    while q:
        t = q.popleft()
        for i in G[t]:
            if not visited[i]:
                if i == a or i == b:
                    return visited[t]
                visited[i] = visited[t] + 1
                q.append(i)


N, M = map(int,input().split())

G = [[] for i in range(N+1)]
for i in range(M):
    s, e = map(int,input().split())
    G[s].append(e)
    G[e].append(s)
res = []
min_sum = 9999999999
for i in range(1,N):
    for j in range(i+1,N+1):
        sum_ = 0
        for k in range(1,N+1):
            if k!=i and k!=j:
                sum_ += dfs(i,j,k)
        if min_sum > sum_:
            min_sum = sum_
            a,b,c = i,j,2*min_sum


print(a,b,c)



