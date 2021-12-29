# k번째 수

def solution(array, commands):
    n = len(commands)
    answer = []
    for s in range(n):
        i = commands[s][0] - 1
        j = commands[s][1]
        k = commands[s][2] - 1

        target_list = array[i:j]
        target_list.sort()
        answer.append(target_list[k])

    return answer