dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, arr, s):
    arr[x][y] = 0
    stack.append([x, y])
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == s:
                arr[nx][ny] = 0
                stack.append([nx, ny])
N = int(input())

arr1 = [list(input()) for _ in range(N)]
arr2 = []

stack = []
for i in range(N):
    k = []
    for j in range(N):
        if arr1[i][j] == 'G':
            k.append('R')
        else:
            k.append(arr1[i][j])
    arr2.append(k)

ans1 = 0
ans2 = 0

for i in range(N):
    for j in range(N):
        if arr1[i][j] == 'R':
            dfs(i, j, arr1, 'R')
            ans1 += 1
        elif arr1[i][j] == 'B':
            dfs(i, j, arr1, 'B')
            ans1 += 1
        elif arr1[i][j] == 'G':
            dfs(i, j, arr1, 'G')
            ans1 += 1
        if arr2[i][j] == 'R':
            dfs(i, j, arr2, 'R')
            ans2 += 1
        elif arr2[i][j] == 'B':
            dfs(i, j, arr2, 'B')
            ans2 += 1

print(f"{ans1} {ans2}")


