
# skill의 각 행은 [type, r1, c1, r2, c2, degree]
# type = {1:적,2:아군}
# (r1,c1) ~ (r2,c2) 까지 공격
# return = 파괴되지 않은 건물의 개수

# 누적합을 이용한 효율성 개선

def solution(board, skill):
    answer = 0
    M = len(board[0])
    N = len(board)
    temp = [[0 for _ in range(M+1)] for _ in range(N+1)]
    for tp, r1, c1, r2, c2, degree in skill:
        if tp == 1:
            temp[r1][c1] -= degree
            temp[r2+1][c2+1] -= degree
            temp[r1][c2+1] += degree
            temp[r2+1][c1] += degree
        else:
            temp[r1][c1] += degree
            temp[r2+1][c2+1] += degree
            temp[r1][c2+1] -= degree
            temp[r2+1][c1] -= degree

    for i in range(N):
        for j in range(M):
            temp[i][j+1] += temp[i][j]

    for i in range(M):
        for j in range(N):
            temp[j+1][i] += temp[j][i]

    for i in range(N):
        for j in range(M):
            if board[i][j] + temp[i][j] > 0:
                answer += 1

    return answer


print(solution([[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]], [
    [1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]))
