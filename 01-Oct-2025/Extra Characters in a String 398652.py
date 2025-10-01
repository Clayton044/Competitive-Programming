# Problem: Extra Characters in a String - https://leetcode.com/problems/extra-characters-in-a-string/description/

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        word_set = set(dictionary)
        dp = [0] * (n + 1)
        
        for i in range(n - 1, -1, -1):
            # Option 1: skip s[i], count it as extra
            dp[i] = dp[i + 1] + 1
            # Option 2: try to match a word starting at i
            for j in range(i, n):
                if s[i:j+1] in word_set:
                    dp[i] = min(dp[i], dp[j+1])
                    
        return dp[0]