m = 100000000000


def dfs(total, cur, visited, name):
    global m
    flag = False
    for idx, i in enumerate(visited):
        if i[2] == False and name[idx] != 'A':
            flag = True
    if flag == False:
        m = min(m, total-1)
        return
    total += 1

    if visited[cur][0] == False:  # forward = false
        if visited[cur][2] == False:  # visited = false
            visited[cur][0] = True
            visited[cur][2] = True
            if cur < len(name)-1:
                dfs(total + min(ord(name[cur])-ord('A'), ord('Z') -
                    ord(name[cur])+1), cur+1, visited, name)
            else:
                dfs(total + min(ord(name[cur])-ord('A'), ord('Z') -
                    ord(name[cur])+1), 0, visited, name)
            visited[cur][0] = False
            visited[cur][2] = False
        else:  # visited = true
            visited[cur][0] = True
            if cur < len(name)-1:
                dfs(total, cur+1, visited, name)
            else:
                dfs(total, 0, visited, name)
            visited[cur][0] = False

    if visited[cur][1] == False:  # backward = false
        if visited[cur][2] == False:  # visited = false
            visited[cur][1] = True
            visited[cur][2] = True
            if cur >= 1:
                dfs(total + min(ord(name[cur])-ord('A'), ord('Z') -
                    ord(name[cur])+1), cur-1, visited, name)
            else:
                dfs(total + min(ord(name[cur])-ord('A'), ord('Z') -
                    ord(name[cur])+1), len(name)-1, visited, name)

            visited[cur][1] = False
            visited[cur][2] = False
        else:  # visited = true
            visited[cur][1] = True
            if cur >= 1:
                dfs(total, cur-1, visited, name)
            else:
                dfs(total, len(name)-1, visited, name)
            visited[cur][1] = False


def solution(name):
    answer = 0
    visited = [[False, False, False] for i in range(len(name))]  # 0 forward, 1 backward, 2 visited

    dfs(0, 0, visited, name)
    if m < 0:
        return answer
    else:
        return m


print(solution("AAABAAAAAB"))
