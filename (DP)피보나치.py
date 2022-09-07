
c = input()

def dfs(count):
    if count == 0:
        return 0
    elif count == 1 or count == 2:
        return 1
    else:
        return dfs(count-1)+dfs(count-2)

def solution(n):
    return dfs(n)
    

print(solution(int(c)))