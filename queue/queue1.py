# 기능개발

from collections import deque


def solution(progresses, speeds):
    answer = []

    queue_work = deque(progresses)
    queue_speed = deque(speeds)

    day = 0

    while queue_work:
        cnt = 0
        if (100 - queue_work[0] - (day * queue_speed[0])) % queue_speed[0] == 0:
            day += (100 - queue_work[0] - (day * queue_speed[0])) // queue_speed[0]
        else:
            day += ((100 - queue_work[0] - (day * queue_speed[0])) // queue_speed[0]) + 1
        queue_work.popleft()
        queue_speed.popleft()
        cnt += 1

        while queue_work:
            if queue_work[0] + (day * queue_speed[0]) >= 100:
                queue_work.popleft()
                queue_speed.popleft()
                cnt += 1
                continue
            else:
                break

        answer.append(cnt)

    return answer