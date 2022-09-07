from collections import defaultdict
from itertools import combinations

# a*b*c = abc로 조합가능한 모든 경우의 수
# 하지만 안입는 경우도 존재하기 때문에 각각 +1을 해줌
# 하지만 abc 전부 안입는 경우는 제외해야 하므로 -1


def solution(clothes):
    d = defaultdict(list)
    for i in clothes:
        d[i[1]] = d[i[1]] + [i[0]]

    answer = 1
    for key in d:
        answer *= len(d[key]) + 1

    return answer - 1


print(solution([["yellow_hat", "headgear"], [
      "blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
