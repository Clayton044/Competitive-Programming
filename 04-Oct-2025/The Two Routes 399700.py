# Problem: The Two Routes - https://codeforces.com/problemset/problem/601/A

from collections import deque

def bfs(graph, n):
    """Returns shortest distance from node 1 to n using BFS."""
    dist = [-1] * (n + 1)
    dist[1] = 0
    q = deque([1])

    while q:
        node = q.popleft()
        for nei in graph[node]:
            if dist[nei] == -1:
                dist[nei] = dist[node] + 1
                q.append(nei)
    return dist[n]

def solve():
    n, m = map(int, input().split())
    rail = [[0] * (n + 1) for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, input().split())
        rail[u][v] = rail[v][u] = 1

    # Build graphs for railway and road
    rail_graph = [[] for _ in range(n + 1)]
    road_graph = [[] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j:
                if rail[i][j]:
                    rail_graph[i].append(j)
                else:
                    road_graph[i].append(j)

    train_time = bfs(rail_graph, n)
    bus_time = bfs(road_graph, n)

    # If either cannot reach destination
    if train_time == -1 or bus_time == -1:
        print(-1)
    else:
        print(max(train_time, bus_time))

if __name__ == "__main__":
    solve()
