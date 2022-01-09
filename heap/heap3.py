# 이중우선순위큐

import heapq as hq


def solution(operations):
    min_heap = []

    for i in range(len(operations)):
        if not min_heap and operations[i][0] == 'D':
            continue

        if operations[i][0] == 'I':
            hq.heappush(min_heap, int(operations[i][1:]))
        elif operations[i] == 'D -1':
            hq.heappop(min_heap)
        else:
            min_heap.pop()

    if min_heap:
        return [max(min_heap), min(min_heap)]
    else:
        return [0, 0]


print(solution(["I 7", "I 5", "I -5", "D -1"]))  # [7,5]