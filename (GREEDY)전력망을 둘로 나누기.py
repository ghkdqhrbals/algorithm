from collections import deque


# node 1과 연결되는 최대 노드 개수
def bfs(start, n, graph):
    visited = [False for i in range(n+1)]
    q = deque([start])
    visited[start] = True
    result = 1
    while q:
        current_node = q.popleft()
        for connected_node, v in enumerate(graph[current_node]):
            if v == 1 and visited[connected_node]==False:
                q.append(connected_node)
                visited[connected_node] = True
                result += 1
    return result
        
    
    
    
def solution(n, wires):
    m = 100
    answer = -1
    graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
    check = [False for _ in range(len(wires))]
    for wire in wires:
        graph[wire[0]][wire[1]] = 1
        graph[wire[1]][wire[0]] = 1
    for i in range(len(wires)):
        graph[wires[i][0]][wires[i][1]] = 0
        graph[wires[i][1]][wires[i][0]] = 0
        m = min(abs(n-2*bfs(1, n, graph)), m)
        graph[wires[i][0]][wires[i][1]] = 1
        graph[wires[i][1]][wires[i][0]] = 1

    return m


print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
print(solution(4, [[1, 2], [2, 3], [3, 4]]))
print(solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]))
