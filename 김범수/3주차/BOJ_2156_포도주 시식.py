def max_list(li):
    if N == 1:
        max_[0] = li[0]
        return max_[0]
    elif N == 2:
        max_[1] = li[0]+li[1]
        return max_[1]
    elif N == 3:
        max_[2] = max(li[0]+li[1],li[1]+li[2],li[0]+li[2])
        return max_[2]
    else:
        max_[0] = li[0]
        max_[1] = li[0]+li[1]
        max_[2] = max(li[0]+li[1],li[1]+li[2],li[0]+li[2])
        for i in range(3,N):
            max_[i] = max(max_[i-2] + li[i], max_[i-3] +li[i] + li[i-1],max_[i-1])
        return max(max_)

N = int(input())
li = []
for i in range(N):
    li.append(int(input()))

max_ = [0]*N
print(max_list(li))