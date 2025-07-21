# Problem: From adjacency list to adjacency matrix - https://basecamp.eolymp.com/en/problems/3982

# example below, replace it with your solution
n = int(input())
adj =  [[0] * n for idx in range(n)]

for idx in range(n):
    inp = list(map(int, input().split()))
    for inIdx in inp[1:]:
        adj[idx][inIdx - 1] = 1

for i in adj:
    print(' '.join(map(str, i)))