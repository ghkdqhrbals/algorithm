from itertools import permutations, combinations


def solution(word):
    answer = 0

    def getcount(num, w):
        s = set()
        for i in permutations(w, num):
            s.add("".join(i))
        return s

    for i in range(1, len(word)):
        print(getcount(i, word))

    return answer


print(solution("AAAAE"))
