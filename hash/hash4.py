# 베스트엘범
import operator


def solution(genres, plays):
    genre_sum = {}
    select = {}

    for i in set(genres):
        genre_sum[i] = 0
        select[i] = []  # [고유번호, play수] 집어넣을거임
    for i in range(len(genres)):
        genre_sum[genres[i]] += plays[i]

    genre_sum = sorted(genre_sum.items(), key=operator.itemgetter(1), reverse=True)

    for i in range(len(genres)):
        if len(select[genres[i]]) == 2:
            if select[genres[i]][1][1] >= plays[i]:
                continue
            else:
                if select[genres[i]][0][1] >= plays[i]:
                    select[genres[i]][1] = [i, plays[i]]
                else:
                    select[genres[i]].pop()
                    select[genres[i]].insert(0, [i, plays[i]])
        elif len(select[genres[i]]) == 1:
            if select[genres[i]][0][1] >= plays[i]:
                select[genres[i]].append([i, plays[i]])
            else:
                select[genres[i]].insert(0, [i, plays[i]])
        else:
            select[genres[i]].append([i, plays[i]])

    answer = []
    for i in range(len(genre_sum)):
        for j in range(len(select[genre_sum[i][0]])):
            answer.append(select[genre_sum[i][0]][j][0])

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
# [4, 1, 3, 0]