# 더 맵게
import heapq


def solution(scoville, K):
    answer = 0
    scoville.sort()

    while scoville[0] < K:
        if len(scoville) <= 1:
            return -1

        first_small = heapq.heappop(scoville)
        second_small = heapq.heappop(scoville)
        new_K = first_small + (second_small * 2)
        answer += 1

        heapq.heappush(scoville, new_K)

    return answer