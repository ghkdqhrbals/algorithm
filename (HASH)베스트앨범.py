from collections import defaultdict


def solution(genres, plays):
    answer = []
    d1 = defaultdict(list)
    d2 = defaultdict(int)

    for idx, i in enumerate(zip(genres, plays)):
        d1[i[0]] = d1[i[0]]+[[idx, i[1]]]
        d2[i[0]] += i[1]

    d2 = sorted(d2.items(), key=lambda x: x[1], reverse=True)
    print(d1)
    for i in d2:
        t = 0
        for j in sorted(d1[i[0]], key=lambda x: x[1], reverse=True):
            if t == 2:
                break
            answer.append(j[0])
            t += 1

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 500, 500, 500, 500]))
