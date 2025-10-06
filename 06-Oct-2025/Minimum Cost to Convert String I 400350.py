# Problem: Minimum Cost to Convert String I - https://leetcode.com/problems/minimum-cost-to-convert-string-i/description/?envType=problem-list-v2&envId=shortest-path

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        INF = float('inf')
        dist = [[INF] * 26 for _ in range(26)]

        
        for i in range(26):
            dist[i][i] = 0

        
        for o, c, w in zip(original, changed, cost):
            u, v = ord(o) - 97, ord(c) - 97
            dist[u][v] = min(dist[u][v], w)

        
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        total_cost = 0
        for a, b in zip(source, target):
            if a == b:
                continue
            u, v = ord(a) - 97, ord(b) - 97
            if dist[u][v] == INF:
                return -1
            total_cost += dist[u][v]

        return total_cost