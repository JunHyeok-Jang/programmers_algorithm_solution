# 네트워크

def bfs(node, adj):
    queue = [node]
    visited = [0 for _ in range(len(adj))]
    visited[node] = 1

    while queue:
        v = queue.pop(0)

        for i in range(len(adj[v])):
            if visited[adj[v][i]] == 0:
                queue.append(adj[v][i])
                visited[adj[v][i]] = 1
    return visited


def solution(n, computers):
    adj = [[] for _ in range(len(computers))]
    for i in range(len(computers)):
        info = computers[i]
        for j in range(len(info)):
            if i == j:
                continue
            else:
                if info[j] == 1:
                    adj[i].append(j)

    visited = [0 for _ in range(len(computers))]
    answer = 0
    while any(0 == i for i in visited):
        node = visited.index(0)
        answer += 1
        return_visited = bfs(node, adj)
        visited = [x + y for x, y in zip(visited, return_visited)]

    return answer