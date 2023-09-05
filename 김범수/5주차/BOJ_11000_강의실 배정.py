import sys
import heapq
input = sys.stdin.readline
N = int(input())
li = [list(map(int,input().split())) for i in range(N)]
li.sort()

hq = []
heapq.heappush(hq,li[0][1])

for i in range(1,N):
    if li[i][0] >= hq[0]:
        heapq.heappop(hq)
    heapq.heappush(hq,li[i][1])

print(len(hq))



