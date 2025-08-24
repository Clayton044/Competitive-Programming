# Problem: E - Knapsack 2 - https://atcoder.jp/contests/dp/tasks/dp_e

data = input().split()

n = int(data[0])
W = int(data[1])

items = []
index = 2
total_value = 0
for i in range(n):
    w = int(data[index])
    v = int(data[index + 1])
    items.append((w, v))
    total_value += v
    index += 2


INF = float('inf')
dp = [INF] * (total_value + 1)
dp[0] = 0  


for weight, value in items:
    
    for val in range(total_value, value - 1, -1):
        if dp[val - value] != INF:
            dp[val] = min(dp[val], dp[val - value] + weight)


answer = 0
for value in range(total_value, -1, -1):
    if dp[value] <= W:
        answer = value
        break

print(answer)
