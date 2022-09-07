




def solution2(citations):
    citations.sort(reverse=True)
    for idx , citation in enumerate(citations):
        if idx >= citation:
            return idx
    return len(citations) # 전부 다 cite가 클 때,


print(solution([3, 0, 6, 1, 5]))
print(solution([0,2,4,6,8,10]))