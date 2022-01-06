def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(reverse=True, key=lambda x: (x * 4)[:4])

    if numbers[0] == '0':
        return '0'
    else:
        return ''.join(numbers)


print(solution([3, 30, 34, 5, 9]))  # '9534330'