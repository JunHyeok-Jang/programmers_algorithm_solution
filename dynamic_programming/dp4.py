# 도둑질

def solution(money):
    length = len(money)

    # 첫번째집 안쓰는 경우(마지막집 그냥 문제없이 사용가능)
    answer1 = [0 for _ in range(length)]
    answer1[1] = money[1]
    answer1[2] = max(money[1], money[2])

    for i in range(3, length):
        answer1[i] = max(answer1[i - 1], money[i] + answer1[i - 2])

    # 첫번째집 쓰는경우(마지막집 사용x)
    answer2 = [0 for _ in range(length)]
    answer2[0] = money[0]
    answer2[1] = max(money[0], money[1])
    for i in range(2, length):
        answer2[i] = max(answer2[i - 1], money[i] + answer2[i - 2])

    return max(answer1[-1], answer2[-2])


print(solution([1, 2, 16, 4, 20]))  # 36