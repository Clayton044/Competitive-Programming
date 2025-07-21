# Problem: From Adjacency Matrix to Adjacency List - https://www.eolymp.com/en/contests/9060/problems/78603

n = int(input())
for _ in range(n):
    idx = []
    arr = list(map(int, input().split()))
    for i in range(len(arr)):
        if arr[i] == 1:
            idx.append(i+1)
    ans = [len(idx)] + idx
    print(*ans)