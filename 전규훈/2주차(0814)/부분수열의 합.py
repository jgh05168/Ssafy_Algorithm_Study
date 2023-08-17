N, S = map(int, input().split())

arr = list(map(int, input().split()))

cnt = 0

# 비트연산자를 사용한 전체 부분수열 구하기
for i in range(1, (1 << N)):
    sum = 0
    for j in range(N):
        if i & (1 << j):
            sum += arr[j]

    # 부분수열의 합이 원하는 값과 같을 경우
    if sum == S:
        cnt += 1

print(cnt)
