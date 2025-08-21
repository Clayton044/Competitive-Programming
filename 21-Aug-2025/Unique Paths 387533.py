# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m > n:
            m, n = n, m  
    
        total = m + n - 2
        r = m - 1  
        
        
        numerator = 1
        denominator = 1
        
        for i in range(1, r + 1):
            numerator *= (total - i + 1)
            denominator *= i
        
        return numerator // denominator