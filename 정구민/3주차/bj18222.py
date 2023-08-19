def find(x):
    if x == 1:
        return 1
    if x == 0:
        return 0
    if x%2:
        return 1 - find(x//2)
    if x%2 == 0:
        return find(x//2)

N = int(input())
X = '0'
print(find(N-1))
