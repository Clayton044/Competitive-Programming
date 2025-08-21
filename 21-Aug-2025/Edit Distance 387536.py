# Problem: Edit Distance - https://leetcode.com/problems/edit-distance/description/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
    
        
        if m > n:
            word1, word2 = word2, word1
            m, n = n, m

        
        dp = list(range(m + 1))  
        
        for j in range(1, n + 1):
            prev = dp[0]  
            dp[0] = j     
            
            for i in range(1, m + 1):
                temp = dp[i]  
                if word1[i - 1] == word2[j - 1]:
                    dp[i] = prev  
                else:
                    dp[i] = 1 + min(
                        dp[i - 1],   
                        dp[i],       
                        prev         
                    )
                prev = temp  
        
        return dp[m]