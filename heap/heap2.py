# 디스크 컨트롤러
import heapq
def solution(jobs):
    num = len(jobs)
    wating = []
    jobs.sort(key=lambda x: (x[0], x[1]))

    # 첫번째 작업 수행
    first = jobs.pop(0)
    work_time = first[0] + first[1]  # finish time
    answer = first[1]

    while jobs or wating:
        while jobs and jobs[0][0] <= work_time:  # 작업시간 중 작업요청 들어올 때
            k = jobs.pop(0)
            tp = tuple([k[1], k[0]])
            heapq.heappush(wating, tp)

        if not wating:
            earliest = jobs.pop(0)
            work_time += (earliest[0] - work_time + earliest[1])
            answer += (work_time - earliest[0])
        else:
            smallest = heapq.heappop(wating)
            work_time += smallest[0]
            answer += (work_time - smallest[1])
    return answer // num