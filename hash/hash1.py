# 완주하지 못한 선수
def solution(participant, completion):
    set_parti = set(participant)
    dict_parti = {}
    dict_comple = {}

    for name in set_parti:
        dict_parti[name] = 0
        dict_comple[name] = 0

    for name in participant:
        dict_parti[name] += 1

    for name in completion:
        dict_comple[name] += 1

    # 비교
    for name in set_parti:
        if dict_comple[name] != dict_parti[name]:
            return name