def solution(n, edge):
    answer = 0
    lis = [[] for _ in range(n+1)]
    for [a, b] in edge:
        lis[a].append(b)
        lis[b].append(a)
    visited = [0] * (n+1)
    queue = []
    queue.append(1)
    visited[1] = 1
    while queue:
        t = queue.pop(0)
        for i in lis[t]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[t] + 1
    for i in visited:
        if i == max(visited):
            answer += 1
    return answer

n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, edge))