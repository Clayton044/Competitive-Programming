# Problem: G - Longest Path - https://atcoder.jp/contests/dp/tasks/dp_g

from collections import defaultdict, deque

data = input().split()

n = int(data[0])
m = int(data[1])


graph = defaultdict(list)
indegree = [0] * (n + 1)  

index = 2
for _ in range(m):
    x = int(data[index])
    y = int(data[index + 1])
    graph[x].append(y)
    indegree[y] += 1
    index += 2



dp = [0] * (n + 1)


queue = deque()


for i in range(1, n + 1):
    if indegree[i] == 0:
        queue.append(i)


while queue:
    u = queue.popleft()
    for v in graph[u]:
        
        dp[v] = max(dp[v], dp[u] + 1)
        indegree[v] -= 1
        if indegree[v] == 0:
            queue.append(v)


print(max(dp))