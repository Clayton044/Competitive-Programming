# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(city):
            for neighbor, connected in enumerate(isConnected[city]):
                if connected and not visited[neighbor]:
                    visited[neighbor] = True
                    dfs(neighbor)

        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        for i in range(n):
            if not visited[i]:
                dfs(i)
                provinces += 1

        return provinces