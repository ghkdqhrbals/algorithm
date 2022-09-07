# 최단거리는 bfs?
from collections import deque

def bfs(x,y,maps):
    n=len(maps)
    m=len(maps[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    q = deque([(x,y,1)])
    visited[x][y]=True
    while q:
        tx,ty,result = q.popleft()
        if tx == n-1 and ty == m-1:
            return result
        
        if tx+1 < n and visited[tx+1][ty] == False and maps[tx+1][ty] == 1:
            q.append((tx+1,ty,result+1))
            visited[tx+1][ty]=True # 넣을 때 True 하는게 속도측면 더빠름. 아니면 한번씩 다 넣어버리고 꺼냄.
        if ty-1 >=0 and visited[tx][ty-1] == False and maps[tx][ty-1] == 1:
            q.append((tx,ty-1,result+1))
            visited[tx][ty-1]=True
        if tx-1 >=0 and visited[tx-1][ty] == False and maps[tx-1][ty] == 1:
            q.append((tx-1,ty,result+1))
            visited[tx-1][ty]=True
        if ty+1 < m and visited[tx][ty+1] == False and maps[tx][ty+1] == 1:
            q.append((tx,ty+1,result+1))
            visited[tx][ty+1]=True
        
    

def solution(maps):
    answer = 0
    answer = bfs(0,0,maps)
    
    if answer == None:
        return -1
    
    return answer

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))