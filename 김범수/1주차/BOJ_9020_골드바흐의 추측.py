import math
#소수 만들기 (10000이하) 만큼
N = 10000
prime =[1 for i in range(N+1)]

prime[0] = 0
prime[1] = 0

for i in range(2,int(math.sqrt(N)+1)):
    if prime[i]==1:
        k = 2
        while i*k <= N:
            prime[i*k] = 0
            k += 1
####
T = int(input())
for _ in range(1,T+1):
    # 만들고자하는 짝수 입력
    N = int(input())
    # 짝수의 2/1 지점부터 +1, -1 하면서 소수 찾기
    for i in range(N//2):
        print('#',N//2 +i,N//2 -i)
        if prime[N//2 +i] and prime[N//2 -i]:
            print(N//2 -i,N//2 +i)
            
            break

'''
1
8
'''
