def solution(n, edge):
    li = [[]for _ in range(n+1)]
    visited = [0]*(n+1)
    for i in edge:
        s,e = i
        li[s].append(e)
        li[e].append(s)
    stack = [1]
    stack2 = [1]
    while stack:
        v = stack.pop(0)
        k = stack2.pop(0)
        visited[v] = k
        for i in li[v]:
            if not visited[i]and not i in stack:
                stack.append(i)
                stack2.append(k+1)
    res = max(visited)
    
    kk = 0
    for i in visited:
        if i == res: 
            kk += 1
    return kk
            
            
        
        