# Problem: Path With Minimum Effort - https://leetcode.com/problems/path-with-minimum-effort/description/

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0
        heap = [(0, 0, 0)]  # (effort, row, col
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        
        while heap:
            effort, i, j = heapq.heappop(heap)
            
            if i == m-1 and j == n-1:  # Reached bottom-righ
                return effort
                
            if effort > dist[i][j]:
                continue
                
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    new_effort = max(effort, abs(heights[ni][nj] - heights[i][j]))
                    if new_effort < dist[ni][nj]:
                        dist[ni][nj] = new_effort
                        heapq.heappush(heap, (new_effort, ni, nj))
                        
        return dist[m-1][n-1]