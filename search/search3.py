# 카펫

def get_division(num):
    return_list = []
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            return_list.append(i)
            if i ** 2 != num:
                return_list.append(num // i)
    return_list.sort()
    return return_list


def solution(brown, yellow):
    sum_block = brown + yellow
    divisor = get_division(sum_block)

    i, j = 0, -1
    for _ in range(len(divisor)):
        edge = divisor[j] * 2 + (divisor[i] - 2) * 2
        if edge == brown:
            return [divisor[j], divisor[i]]
        i += 1
        j -= 1


print(solution(10, 2))  # [4,3]