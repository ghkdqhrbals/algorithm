from collections import deque



def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    graph = [[0 for _ in range(102)] for _ in range(102)]
    visited = [[False for _ in range(102)] for _ in range(102)]
    delta = ((-1, 0), (0, 1), (1, 0), (0, -1))
    # 테두리
    for i in rectangle:
        for j in range(2*i[0],2*i[2]+1):
            graph[j][2*i[1]] = 1
            graph[j][2*i[3]] = 1
        for j in range(2*i[1],2*i[3]+1):
            graph[2*i[0]][j] = 1
            graph[2*i[2]][j] = 1
            
    # 내부 겹치는 부분 제거
    for i in rectangle:
        for j in range(2*i[0]+1,2*i[2]):
            for z in range(2*i[1]+1,2*i[3]):
                graph[j][z]=0
    
    minimum = 10000000000
    
    q = deque([(2*characterX,2*characterY,0)])
    visited[2*characterX][2*characterY]=True
    while q:
        x,y,length = q.popleft()
        if x == 2*itemX and y == 2*itemY:
            minimum = min(minimum,length)
            print(minimum)
            continue
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 102 and 0 <= ny < 102:
                if graph[nx][ny] == 1 and visited[nx][ny] == False:
                    q.append((nx,ny,length+1))
                    visited[nx][ny]=True
        
    
    return minimum//2


print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]],1,3,7,8))