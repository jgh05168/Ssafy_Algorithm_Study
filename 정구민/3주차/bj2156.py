N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))
dp = [0] * 10000
dp[0] = arr[0]
if N > 1:
    dp[1] = arr[0] + arr[1]
if N > 2:
    dp[2] = max(arr[0]+arr[2], arr[1]+arr[2], dp[1])
for i in range(3, len(arr)):
    dp[i] = max(arr[i] + dp[i-2], arr[i] + arr[i-1] + dp[i-3], dp[i-1])
print(max(dp))