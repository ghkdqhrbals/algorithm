from collections import deque

# ["최소 필요 피로도", "소모 피로도"]

m = -1


def solution(k, dungeons):
    global m
    visited = [False for i in range(len(dungeons))]

    def dfs(cnt, cur_k, k, visited, dungeons):  # cnt : count | cur_k : 피로도 잔량
        global m
        f = True
        for idx, i in enumerate(dungeons):
            if visited[idx] == False and cur_k >= i[0]:
                visited[idx] = True
                dfs(cnt+1, cur_k-i[1], k, visited, dungeons)
                visited[idx] = False
                f = False
        if f:
            m = max(m, cnt)

    dfs(0, k, k, visited, dungeons)
    if m == 0:
        return -1
    return m


print(solution(80, [[80, 20], [50, 40], [30, 10]]))
