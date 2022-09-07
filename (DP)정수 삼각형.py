from collections import deque


def solution2(triangle):
    answer = 0
    q = deque([(triangle[0][0], 0, 0)])  # sum / current index / layer

    while q:

        total_cost, cur, layer = q.popleft()
        if answer <= total_cost:
            answer = total_cost
        if layer == len(triangle)-1:
            continue
        for i in range(2):
            q.append((total_cost+triangle[layer+1][cur+i], cur+i, layer+1))

    return answer


def solution(triangle):
    answer = 0

    for num_layer, cur_layer in enumerate(triangle):
        if num_layer == 0:
            continue
        for cur_index in range(num_layer+1):
            if cur_index == 0:
                cur_layer[cur_index] += triangle[num_layer-1][cur_index]
            elif cur_index == num_layer:
                cur_layer[cur_index] += triangle[num_layer-1][cur_index-1]
            else:
                cur_layer[cur_index] += max(triangle[num_layer-1]
                                            [cur_index-1], triangle[num_layer-1][cur_index])

    return max(triangle[-1])


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
