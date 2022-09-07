# 현재의 state를 저장해야됨
# BFS로 푸는게 맞아보이긴 하는데, route(visited)또한 저장해야됨
# 둘 다 해볼것임
from collections import deque

# bfs queue


def bfs_solution(k, dungeons):
    answer = -1
    d = deque()
    for index, i in enumerate(dungeons):
        if i[0] <= k:
            d.append((k-i[1], [index]))
    while d:
        left, route = d.popleft()
        answer = max(answer, len(route))
        for index, i in enumerate(dungeons):
            if index in route:
                continue
            if i[0] <= left:
                d.append((left-i[1], route+[index]))
    if answer == 0:
        return -1
    return answer


# dfs recursive
def dfs_solution_recur(k, dungeons):
    answer = -1
    visited = [False for _ in dungeons]

    def dfs(count, left, visited):
        print(visited)
        nonlocal answer
        if answer < count:
            answer = count
        for index, i in enumerate(dungeons):
            if visited[index] == False and i[0] <= left:
                visited[index] = True
                dfs(count+1, left-i[1], visited)
                visited[index] = False

    for index, i in enumerate(dungeons):
        if i[0] <= k:
            visited[index] = True
            dfs(1, k-i[1], visited)
            visited[index] = False

    return answer


# dfs stack
def dfs_solution_stack(k, dungeons):
    answer = -1

    for index, i in enumerate(dungeons):
        if i[0] <= k:
            d = deque()
            d.append((k-i[1], [index], 1))

            while d:
                left, route, count = d.pop()
                if answer < count:

                    answer = count
                for index, i in enumerate(dungeons):
                    if i[0] <= left and index not in route:
                        d.append((left-i[1], route+[index], count+1))

    return answer


#print(bfs_solution(80, [[80, 20], [50, 40], [30, 10]]))
print(dfs_solution_stack(80, [[80, 20], [50, 40], [30, 10]]))
