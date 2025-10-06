# Problem: Find a Safe Walk Through a Grid - https://leetcode.com/problems/find-a-safe-walk-through-a-grid/description/?envType=problem-list-v2&envId=shortest-path

import heapq

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        INF = float('inf')
        damage = [[INF] * n for _ in range(m)]
        damage[0][0] = grid[0][0]
        pq = [(grid[0][0], 0, 0)]  
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        while pq:
            d, x, y = heapq.heappop(pq)
            if d >= health:  
                continue
            if (x, y) == (m - 1, n - 1):
                return True
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    nd = d + grid[nx][ny]
                    if nd < damage[nx][ny]:
                        damage[nx][ny] = nd
                        heapq.heappush(pq, (nd, nx, ny))

        return False