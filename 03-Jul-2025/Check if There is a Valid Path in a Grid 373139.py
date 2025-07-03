# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

    
        dirs = {
            1: {'L', 'R'},
            2: {'U', 'D'},
            3: {'L', 'D'},
            4: {'R', 'D'},
            5: {'L', 'U'},
            6: {'R', 'U'}
        }

    
        delta = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
        opposite = {'L': 'R', 'R': 'L', 'U': 'D', 'D': 'U'}

        queue = deque([(0, 0)])
        visited = set([(0, 0)])

        while queue:
            x, y = queue.popleft()
            
            if (x, y) == (m - 1, n - 1):
                return True

            for d in dirs[grid[x][y]]:
                dx, dy = delta[d]
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n:
                
                    if opposite[d] in dirs[grid[nx][ny]] and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny))

        return False