# 다리를 지나는 트럭
def solution(bridge_length, weight, truck_weights):
    if bridge_length == 1:  # 다리길이가 1일 때 종료조건
        return len(truck_weights) * 2

    answer = 1  # 경과시간

    stack = [truck_weights.pop(0)]  # 다리위 트럭
    length_list = [1]

    while truck_weights or stack:
        for i in range(len(length_list)):
            length_list[i] += 1

        if length_list[0] > bridge_length:
            stack.pop(0)
            length_list.pop(0)

        if truck_weights and sum(stack) + truck_weights[0] <= weight:  # 무게에 대해서
            truck = truck_weights.pop(0)
            stack.append(truck)
            length_list.append(1)
        answer += 1

    return answer