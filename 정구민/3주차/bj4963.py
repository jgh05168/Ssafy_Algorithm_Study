import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    visited[x][y] = 1
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= ny < w and 0 <= nx < h:
            if arr[nx][ny] == 1 and not visited[nx][ny]:
                dfs(nx, ny)

dx = [1, 1, 1, -1, -1, -1, 0, 0]
dy = [1, 0, -1, 1, 0, -1, 1, -1]

while True:
    w, h = map(int, input().split()) # 1은 땅, 0은 바다.
    arr = []
    ans = 0
    if w == 0 and h == 0: break
    visited = [[0] * w for _ in range(h)]
    for _ in range(h):
        arr.append(list(map(int, input().split())))
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                ans += 1
    print(ans)
