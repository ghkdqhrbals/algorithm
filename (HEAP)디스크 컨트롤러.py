from collections import deque


def solution(jobs):
    answer = 0
    jobs.sort(key=lambda x: (x[0], x[1]), reverse=False)

    q = deque(jobs)
    t = 0
    total = 0

    while q:

        temp = []
        cur = []
        for i in q:
            if t >= i[0]:  # 예약 대기
                temp.append(i)
            else:  # 아직 멀음
                break
        if len(temp) == 0:
            cur = q.popleft()
        else:
            temp.sort(key=lambda x: x[1], reverse=False)
            q.remove(temp[0])
            cur = temp[0]

        if t < cur[0]:
            t = cur[0]
        if t >= cur[0]:
            t += cur[1]
            total += t - cur[0]

    answer = total//len(jobs)

    return answer


print(solution([[0, 3], [1, 9], [2, 6]]))
