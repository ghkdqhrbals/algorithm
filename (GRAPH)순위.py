
from collections import defaultdict


# 정확하게 순위를 매길 수 있는 선수의 수 return
# 중심 축이 되는 선수 A 확인
def solution(n, results):
    answer = 0
    win_graph = defaultdict(set)    # 이긴 애들
    lose_graph = defaultdict(set)   # 진 애들

    # 확실히 defaultdict로 하니 빈 key 검사 일일이 안해도 됨.
    for i in results:
        win_graph[i[0]] = win_graph[i[0]] | set([i[1]])  # | union
        lose_graph[i[1]] = lose_graph[i[1]] | set([i[0]])

    for i in range(1, n+1):
        for v in win_graph[i]:
            lose_graph[v] = lose_graph[v] | lose_graph[i]
        for v in lose_graph[i]:
            win_graph[v] = win_graph[v] | win_graph[i]

    for i in range(1, n+1):
        temp = len(win_graph[i])+len(lose_graph[i])
        if temp == n-1:
            answer += 1

    return answer


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
print(solution(5, [[2, 1], [2, 3], [2, 4], [2, 2]]))
