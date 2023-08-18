def s(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                continue
            if arr[i][j] == 1:
                for k in range(4):
                    cnt1 = 0
                    for x in range(5):
                        row = j + dx[k]*x
                        col = i + dy[k]*x
                        if 0 <= row < N and 0 <= col < N and arr[col][row] == 1:
                            cnt1 += 1
                    a = j - dx[k]
                    b = i - dy[k]
                    row = row + dx[k]
                    col = col + dy[k]
                    if 0 <= a < N and 0 <= b < N and arr[b][a] == 1:
                        continue
                    if 0 <= row < N and 0 <= col < N and arr[col][row] == 1:
                        continue
                    if cnt1 == 5:
                        print(1)
                        print(i + 1, j + 1)
                        return
            if arr[i][j] == 2:
                for k in range(4):
                    cnt2 = 0
                    for x in range(5):
                        row = j + dx[k]*x
                        col = i + dy[k]*x
                        if 0 <= row < N and 0 <= col < N and arr[col][row] == 2:
                            cnt2 += 1
                        else:
                            if cnt2 > 1:
                                break
                    a = j - dx[k]
                    b = i - dy[k]
                    row = row + dx[k]
                    col = col + dy[k]
                    if 0 <= a < N and 0 <= b < N and arr[b][a] == 2:
                        continue
                    if 0 <= row < N and 0 <= col < N and arr[col][row] == 2:
                        continue
                    if cnt2 == 5:
                        print(2)
                        print(i+1, j+1)
                        return
    print(0)
    return

N = 19
dx = [1, 1, 0, 1]
dy = [-1, 1, 1, 0]
arr = [list(map(int, input().split())) for _ in range(19)]
s(arr)
