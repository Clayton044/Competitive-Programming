# Problem: Knight Probability in Chessboard - https://leetcode.com/problems/knight-probability-in-chessboard/

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]
    
        
        dp = [[0] * n for _ in range(n)]
        dp[row][column] = 1  
        
        for _ in range(k):
            dp_new = [[0] * n for _ in range(n)]
            for r in range(n):
                for c in range(n):
                    if dp[r][c] > 0:
                        for dr, dc in moves:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < n and 0 <= nc < n:
                                dp_new[nr][nc] += dp[r][c] / 8.0
            dp = dp_new
        
        #this too me wayyyyy too much time :D
        return sum(sum(row) for row in dp)