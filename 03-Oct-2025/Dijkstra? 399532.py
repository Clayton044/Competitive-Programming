# Problem: Dijkstra? - https://codeforces.com/problemset/problem/20/C

import sys
import heapq

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))  

dist = [float('inf')] * (n + 1)
parent = [-1] * (n + 1)

dist[1] = 0
pq = [(0, 1)]  

while pq:
    d, u = heapq.heappop(pq)
    if d > dist[u]:
        continue
    for v, w in graph[u]:
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            parent[v] = u
            heapq.heappush(pq, (dist[v], v))

if dist[n] == float('inf'):
    print(-1)
    exit()

path = []
cur = n
while cur != -1:
    path.append(cur)
    cur = parent[cur]
path.reverse()

print(" ".join(map(str, path)))