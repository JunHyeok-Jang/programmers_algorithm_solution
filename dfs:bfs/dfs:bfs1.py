# 타겟넘버

def solution(numbers, target):
    if len(numbers) == 1 and numbers[0] == abs(target):
        return 1
    elif len(numbers) == 1 and numbers[0] != abs(target):
        return 0
    else:
        return solution(numbers[1:], target + numbers[0]) + solution(numbers[1:], target - numbers[0])


print(solution([1, 1, 1, 1, 1], 3))  # 5