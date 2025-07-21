# Problem: Cities and Roads - https://www.eolymp.com/en/contests/9060/problems/78597

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

roads = 0
for i in range(n):
    for j in range(i + 1, n):  # only upper triangle
        if matrix[i][j] == 1:
            roads += 1

print(roads)
