from itertools import permutations


def solution(numbers):
    n = []
    temp = set()

    for j in range(1, len(numbers)+1):
        for i in permutations(numbers, j):
            a = int(("".join(i)))
            temp.add(a)
    if 0 in temp:
        temp.remove(0)
    if 1 in temp:
        temp.remove(1)
    for i in temp:
        f = True
        for z in range(2, int(i**0.5)+1):
            if i % z == 0:
                f = False
                break
        if f:
            n.append(i)
    print(n)
    return len(n)


print(solution("011"))
