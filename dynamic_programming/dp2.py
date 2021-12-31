# 정수 삼각형

def solution(triangle):
    answer = []
    answer.append(triangle[0])
    for k in range(1, len(triangle)):
        answer.append([])
        length = len(triangle[k])

        for i in range(length):
            if i == 0:
                answer[k].append(answer[k - 1][i] + triangle[k][i])
            elif i == (length - 1):
                answer[k].append(answer[k - 1][-1] + triangle[k][-1])
            else:
                answer[k].append(max(answer[k - 1][i], answer[k - 1][i - 1]) + triangle[k][i])
    return max(answer[-1])