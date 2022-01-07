# 주식가격
def solution(prices):
    answer = [0 for _ in range(len(prices))]
    for i in range(len(prices)):
        price = prices[i]

        for j in range(i + 1, len(prices)):
            if price <= prices[j]:
                answer[i] += 1
            else:
                if j == i + 1:
                    answer[i] = 1
                    break
                else:
                    answer[i] += 1
                    break
    answer[-1] = 0
    return answer


print(solution([1, 2, 3, 2, 3]))  # [4, 3, 1, 1, 0]