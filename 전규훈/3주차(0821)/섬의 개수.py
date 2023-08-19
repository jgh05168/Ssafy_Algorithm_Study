import sys
sys.setrecursionlimit(10**6)        # 재귀 구간 증가

#      동 동남 남 남서 서 북서 북 북동
drow = [0, 1, 1, 1, 0, -1, -1, -1]
dcol = [1, 1, 0, -1, -1, -1, 0, 1]

def dfs(row, col):
    if visited[row][col] == True:       # 재귀함수 종료 조건 : 만약 방문한 지역이라면
        return
    else:
        visited[row][col] = True        # 지역 방문 체크
        for d in range(len(drow)):      # 지역의 인접한 8부분에 대한 각각 조사
            nrow = row + drow[d]
            ncol = col + dcol[d]
            # 만약 새로운 좌표가 인덱스의 범위 내에 존재하고, 바다가 아닌 땅이며, 방문하지 않았던 지역이라면
            if 0 <= nrow < h and 0 <= ncol < w and land[nrow][ncol] == 1 and visited[nrow][ncol] == False:
                dfs(nrow, ncol)     # 하나의 섬으로 간주하기 위해 다시 dfs 수행

w, h = map(int, input().split())
while w != 0 or h != 0:
    land = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    island = 0

    # 각각의 경우에 대해 모든 섬 조사
    for row in range(h):
        for col in range(w):
            if land[row][col] == 1 and visited[row][col] == False:
                dfs(row, col)
                island += 1     # 하나의 모든 섬을 탐색했으므로 island += 1

    print(island)
    w, h = map(int, input().split())        # 입력을 다시 받아주는 역할

