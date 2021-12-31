# 프린터

def solution(priorities, location):
    cnt = 0
    pointer = 0

    while priorities:
        pointer = pointer % len(priorities)
        check = priorities[pointer]
        max_prio = max(priorities)

        if check == max_prio:
            cnt += 1
            if pointer == location:
                return cnt
            priorities.pop(pointer)

            if location > pointer:
                location -= 1
            continue
        else:
            pointer += 1