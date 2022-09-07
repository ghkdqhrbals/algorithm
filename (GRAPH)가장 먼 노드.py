from collections import deque

def solution(n, edge):
    answer = 0
    q = deque()
    graph = {i+1:[] for i in range(n)}
    visited = [False for i in range(n)]
    distance = [0 for i in range(n)]
    
    
    for i in edge:
        graph[i[0]] = graph[i[0]] + [i[1]]
        graph[i[1]] = graph[i[1]] + [i[0]]
    
    q.append((1,1))
    visited[0]=True
    distance[0]=1
    while len(q)>0:
        cur, length = q.popleft()

        for node in graph[cur]:
            if visited[node-1]==False:
                q.append((node,length+1))
                distance[node-1]=length+1
                visited[node-1]=True
            else:
                continue    
    return distance.count(max(distance))

print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))