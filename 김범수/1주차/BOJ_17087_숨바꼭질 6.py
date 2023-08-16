# 오늘 배운 유클리드 호제법
# a % b = r1
# b % r1 = r2
# r2 % r3 = 0 -> r3 가 최대 공약수 
def divisor(a,b):
    while b:
        k = a % b
        a = b
        b = k
    return a

# N: 동생, S: 수빈이 위치
N,S = map(int,input().split())
# A list : 동생들 위치들
A = list(map(int,input().split()))

# 동생들 위치 - 수빈이 위치 의 절댓값 리스트(정렬된)
distances = sorted(list(set([abs(i-S) for i in A])))
print(distances)

if len(distances) == 1:
    print(*distances)
else:
    # 5 7 9
    res = distances[0]
    # 큰 수 부터 9부터
    for i in range(len(distances)-1,0,-1):
        res = divisor(distances[i],res)
        print(res)
    print(res)

'''
3 81
33 105 57
'''