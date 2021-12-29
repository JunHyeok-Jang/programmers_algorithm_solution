# 구명보트

def solution(people, limit):
    people.sort()  # 오름차순

    capa = limit

    answer = 1

    i = 0
    j = len(people) - 1

    capa -= people[j]
    j -= 1

    while i <= j:
        if i == j and capa >= people[i]:
            break
        if i == j and capa < people[i]:
            answer += 1
            break

        if capa >= people[j]:
            capa -= people[j]
            j -= 1
            continue
        elif capa >= people[i]:
            capa -= people[i]
            i += 1
            continue
        else:
            answer += 1
            capa = limit

    return answer