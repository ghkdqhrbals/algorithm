


def solution2(phone_book):
    answer = True
    phone_book = sorted(phone_book, key = lambda x:(x))
    for i in range(len(phone_book)-1):
        if phone_book[i]==phone_book[i+1][:len(phone_book[i])]:
            return False
    return answer



def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    print(hash_map)
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                return False
    return answer


print(solution(["119", "97674223", "1195524421","11"]))
print(solution(["12", "1", "2","412","6","413"]))