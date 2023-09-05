N = int(input())
K = int(input())
li = sorted(set(map(int,input().split())))
a = []
for i in range(len(li)-1):
    a.append(li[i+1]-li[i])
a.sort()
if K >= N:
    print(0)
else:
    for i in range(K-1):
        a.pop()
    print(sum(a))