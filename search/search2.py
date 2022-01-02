# 소수찾기

from itertools import permutations

def check_primer(n):
    check_list = [True for _ in range(n+1)]
    check_list[0], check_list[1] = False, False

    for i in range(2, int(n**0.5)+1):
        if check_list[i]:
            j=2
            while i*j <= n:
                if check_list[i*j]:
                    check_list[i*j] = False
                j+=1

    return check_list

def solution(numbers):
    numbers = list(numbers)
    combi = []

    for i in range(1, len(numbers)+1):
        pre = list(permutations(numbers,i))

        for j in range(len(pre)):
            if ''.join(pre[j]) in combi:
                continue
            else:
                combi.append(''.join(pre[j]))

    answer = 0
    check = check_primer(int(max(combi)))

    for i in range(len(combi)):
        if int(combi[i][0]) == 0:
            continue
        else:
            if check[int(combi[i])]:
                answer += 1

    return answer