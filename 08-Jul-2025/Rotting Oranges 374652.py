# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        #this is taking way too much time.        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0)) 
                elif grid[r][c] == 1:
                    fresh += 1

        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        minutes = 0

        
        while queue:
            r, c, time = queue.popleft()
            minutes = max(minutes, time)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # print(nr, nc)
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    # print(fresh)
                    queue.append((nr, nc, time + 1))

        
        return minutes if fresh == 0 else -1