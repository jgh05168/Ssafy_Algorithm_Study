def backtrack(i, arr):

    if i < M:
        for j in range(1, N+1):
            if i == 0:
                arr = []
                arr.append(j)
            else:
                if arr[i-1] <= j:
                    arr.append(j)
                else:
                    continue
            backtrack(i+1, arr)
            arr.pop()
    else:
        print(*arr)


N, M = map(int, input().split())
arr = []
backtrack(0, arr)