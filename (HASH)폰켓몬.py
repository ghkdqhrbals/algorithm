

def solution(nums):
    answer = 0
    s = set(nums)
    if len(s) < len(nums)//2:
        return len(s)
    else:
        return len(nums)//2


print(solution([3, 1, 2, 3]))
