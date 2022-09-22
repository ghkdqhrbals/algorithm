from collections import defaultdict


def solution(N, number):
    answer = -1
    dp = defaultdict(set)

    dp[1].add(N)
    if number == N:
        return 1
    for i in range(2, 9):
        for j in range(0, i-1):
            for p in dp[j+1]:
                for p2 in dp[i-j-1]:
                    dp[i].update([p+p2, p-p2, p*p2, int(str(N) * i)])
                    if p2 != 0:
                        dp[i].update([p//p2])
        print(dp)
        if number in dp[i]:
            return i

    return answer


print(solution(5, 12))
print(solution(2, 11))
