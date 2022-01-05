# 위장

def solution(clothes):
    category = []
    count_list = []
    for i in range(len(clothes)):
        category.append(clothes[i][1])

    for i in set(category):
        count_list.append(category.count(i))

    answer = 1
    for i in range(len(count_list)):
        answer = answer * (count_list[i] + 1)
    return answer - 1