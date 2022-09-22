from collections import defaultdict


def solution(genres, plays):
    answer = []
    # dict ( 장르 : 통합 숫자 )
    dict1 = defaultdict(int)

    # dict ( 장르 : [[번호,숫자]])
    dict2 = defaultdict(list)

    for i in enumerate(zip(genres, plays)):
        dict1[i[1][0]] += i[1][1]
        dict2[i[1][0]] += [[i[0], i[1][1]]]
    sorted_list = sorted(dict1.items(), key=lambda x: (x[1]), reverse=True)
    # print(sorted_list)
    # print(dict2)

    for i in sorted_list:
        sorted_list2 = sorted(dict2[i[0]], key=lambda x: x[1], reverse=True)
        for j in sorted_list2[:2]:
            answer.append(j[0])
#        print(sorted_list2[:2])

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
