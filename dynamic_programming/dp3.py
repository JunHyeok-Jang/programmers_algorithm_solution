# 등굣길

def solution(m, n, puddles):
    index = [[0 for _ in range(m + 1)] for i in range(n + 1)]

    for i in range(len(puddles)):
        index[puddles[i][1]][puddles[i][0]] = -1

    index[0][1], index[1][0] = 0, 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if index[i][j] < 0:
                continue

            index[i][j] = max(index[i - 1][j], index[i][j - 1], (index[i - 1][j] + index[i][j - 1]), 0) % 1000000007

    return index[n][m] % 1000000007