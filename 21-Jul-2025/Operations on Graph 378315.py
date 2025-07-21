# Problem: Operations on Graph - https://www.eolymp.com/en/contests/9060/problems/78602

from collections import defaultdict
n = int(input())
op=int(input())
graph=defaultdict(list)
for i in range(op):
    s = list(map(int, input().split()))
    if s[0] == 1:
        graph[s[1]].append(s[2])
        graph[s[2]].append(s[1])
    else:
        print(*graph[s[1]])
