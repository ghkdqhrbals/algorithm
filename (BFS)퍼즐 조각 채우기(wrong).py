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
                if 0<= nx < n and 0<= ny < n:
                    if board[nx][ny] == flag:
                        board[nx][ny] = -1
                        q.append((nx,ny))
                        result.append([nx,ny])
                        
                        
        # standarlization
        mx = min(result,key= lambda x:x[0])[0]
        my = min(result,key= lambda x:x[1])[1]
        
        for i in range(len(result)):
            result[i][0] -= mx
            result[i][1] -= my
        return result
    
    results_gb = {}
    results_status = {}
    num =0
    # game_board 빈공간 추출 list 저장
    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 0:
                results_gb[num] = bfs(i, j, game_board, 0, n)
                results_status[num] = True
                num+=1
    print(results_gb)
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
                    if not (blocks in results_gb.values()): # (blocks)도형이 빈 공간들과 맞지 않을 때, rotated_table 제자리 및 방문 초기화
                        rotated_table = [row[:] for row in table]
                        visited_t = [[False for _ in range(n)] for _ in range(n)]
                        continue
                        
                    for k, v in results_gb.items():
                        if blocks == v: # blocks도형이 v에 딱 맞을 때, 이걸 뺀 table을 교체
                            if results_status[k]== True:
                                answer+=len(blocks)
                                results_status[k] = False
                                table = [row[:] for row in rotated_table]
                                break
    print(table)
    return answer


print(solution([[0,0,0],[1,0,1],[1,1,0]],[[0,0,0],[0,0,0],[1,0,1]]))