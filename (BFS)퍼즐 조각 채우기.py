from collections import deque

def solution(game_board, table):
    answer = 0
    n = len(game_board)
    direction = ((1,0),(-1,0),(0,1),(0,-1))
    gb_list = []
    visited_gb = [[False for _ in range(n)] for _ in range(n)]
    visited_t = [[False for _ in range(n)] for _ in range(n)]
    # game_board 에서 0이고 방문 안한곳, 도형을 list에 저장
    
    def get_s(game_board,visited, num):
        for i in range(n):
            for j in range(n):
                if game_board[i][j] == num and visited[i][j]==False:
                    return [i,j]
        return [-1,-1]
    
    def bfs(startx, starty, board, flag, n):
        q = deque([(startx,starty)])
        result = [[startx,starty]]
        board[startx][starty] = -1
        while q:
            x,y = q.popleft()
            
            for dx,dy in direction:
                nx, ny = x+dx, y+dy
                if 0 <= nx < n and 0 <= ny < n:
                    if board[nx][ny] == flag:
                        board[nx][ny] = -1
                        q.append((nx,ny))
                        result.append([nx,ny])
                        
                        
        # standarlize
        mx = min(result,key= lambda x:x[0])[0]
        my = min(result,key= lambda x:x[1])[1]
        
        for i in range(len(result)):
            result[i][0] -= mx
            result[i][1] -= my
        return result
    
    block = []
    
    num =0
    # game_board 빈공간 추출 list 저장
    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 0:
                block.append(bfs(i, j, game_board, 0, n))
                
    for _ in range(4):
        table = [list(row)[::-1] for row in zip(*table)]
        rotated_table = [row[:] for row in table]
        visited_t = [[False for _ in range(n)] for _ in range(n)] # 에러검출
        for i in range(n):
            for j in range(n):
                # 회전된 도형과 매칭
                if rotated_table[i][j] == 1:
                    rotated_table[i][j] = -1
                    blocks = bfs(i,j,rotated_table ,1,n)
                    if blocks in block: # (blocks)도형들이 빈 공간들(block)과 맞을 때, 빈 공간 지우기 및 테이블에서 도형 지우기
                        block.pop(block.index(blocks))
                        answer+=len(blocks)
                        table = [row[:] for row in rotated_table]
                    else:
                        rotated_table = [row[:] for row in table]
                        
    print(table)
    return answer

# print(solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]],
#                [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]))




# A 에 빈공간 2개, B 에 도형 1개 => 빈공간 중복적용 불가능하도록 설정 !!!>> 여기가 잘못되어있네 <<!!!
#print(solution([[0,0,1],[1,1,1],[0,0,1]],[[0,0,0],[0,0,0],[1,1,0]]))

# A 에 빈공간 1개, B 에 도형 2개 => 도형 한번만 적용되도록 설정
#print(solution([[0,0,1],[0,0,1],[1,1,1]],[[1,1,0],[1,1,0],[0,0,0]]))

# A 에 작은공간 2개, B 에 도형 1개
print(solution([[0,0,0],[1,0,1],[1,1,0]],[[0,0,0],[0,0,0],[1,0,1]]))