# Problem: Regular Graph - https://basecamp.eolymp.com/en/problems/5076

n, m = map(int, input().split())
degree = [0] * (n + 1)
for _ in range(m):
    u, v = map(int, input().split())
    degree[u] += 1
    degree[v] += 1
d = degree[1]
print("YES" if all(degree[i] == d for i in range(2, n + 1)) else "NO")