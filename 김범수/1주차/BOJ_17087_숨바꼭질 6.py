def divisor(a,b):
    while b:
        k = a % b
        a = b
        b = k
    return a
        
N,S = map(int,input().split())
A = list(map(int,input().split()))
distances = sorted(list(set([abs(i-S) for i in A])))
if len(distances) == 1:
    print(*distances)
else:
    res = distances[0]
    for i in range(len(distances)-1,0,-1):
        res = divisor(distances[i],res)
    print(res)

