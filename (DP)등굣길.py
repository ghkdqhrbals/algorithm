
from collections import deque


def solution(m, n, puddles):
    answer = 0
    visited = [[0 for i in range(n)] for j in range(m)]
    q = deque([([0,0])])
    visited[0][0]=1
    
    while q:
        cur_p= q.popleft()
        x=cur_p[0]
        y=cur_p[1]
        
        
        
        
        if x+1 < m and visited[x+1][y] == 0 and not [x+2,y+1] in puddles: # 오른쪽
            if y-1 >= 0: # 위쪽
                visited[x+1][y] = visited[x][y]+visited[x+1][y-1]
                q.append([x+1,y])
            else:
                visited[x+1][y] = visited[x][y]
                q.append([x+1,y])
        if y+1 < n and visited[x][y+1] == 0 and not [x+1,y+2] in puddles: # 아래쪽
            if x-1 >= 0:
                visited[x][y+1] = visited[x][y]+visited[x-1][y+1]
                q.append([x,y+1])
            else:
                visited[x][y+1] = visited[x][y]
                q.append([x,y+1])
    #print(visited)
            

    return visited[m-1][n-1] % 1000000007


print(solution(4, 3, [[2, 2]]))
print(solution(2, 2, [[2, 1]]))
