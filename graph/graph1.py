# 가장 먼 노드

def solution(n, edge):
    rank = [0] * (n + 1)
    adj = [[] for _ in range(n + 1)]

    for v in edge:  # make adj_list
        v1 = v[0]
        v2 = v[1]
        adj[v1].append(v2)
        adj[v2].append(v1)

    # bfs
    visited = [0 for _ in range(n + 1)]
    queue = [1]
    visited[1] = 1
    while queue:
        parent = queue.pop(0)

        for node in adj[parent]:
            if visited[node] == 0:
                queue.append(node)
                visited[node] = 1
                rank[node] = rank[parent] + 1
            else:
                continue

    max_depth = max(rank)
    answer = rank.count(max_depth)
    return answer