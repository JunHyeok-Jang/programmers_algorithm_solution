# 모의고사
def solution(answers):
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    cnt1 = 0
    cnt2 = 0
    cnt3 = 0

    for i in range(len(answers)):
        if answers[i] == student1[i % 5]:
            cnt1 += 1
        if answers[i] == student2[i % 8]:
            cnt2 += 1
        if answers[i] == student3[i % 10]:
            cnt3 += 1

    max_num = max(cnt1, cnt2, cnt3)
    return_list = []

    if cnt1 == max_num:
        return_list.append(1)
    if cnt2 == max_num:
        return_list.append(2)
    if cnt3 == max_num:
        return_list.append(3)

    return return_list