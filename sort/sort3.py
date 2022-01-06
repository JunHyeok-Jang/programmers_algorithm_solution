# H-index

def solution(citations):
    citations.sort(reverse=True)
    h = 0

    if citations[0] == 0:  # 논문 인용횟수 전부 0인 경우
        return h

    for i in range(len(citations)):
        if h == citations[i]:
            return h

        if h <= citations[i]:
            h += 1
        else:
            break

    return h