# 문제 : https://school.programmers.co.kr/learn/courses/30/parts/12081

# 풀이1 arr의 원소를 하나씩 돌면서 다음 숫자를 만나면 POP하고 다른 숫자를 
#       만나면 
# def solution(arr): 
#     temp = arr[0]
#     j = 0
#     for i in arr[1:]:
#         if temp == i:
#             arr.pop(j+1)
#             j -= 1
#         else:
#             temp = i
#         j += 1
#     arr
#     return arr

# 풀이2
def solution(arr):
    answer = []
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            answer.append(arr[i])
        if i+1 == len(arr)-1:
            answer.append(arr[i+1])
    return answer