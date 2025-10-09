# Problem: Find Beautiful Indices in the Given Array I - https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-i/description/

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        def kmp_search(text, pattern):
            n, m = len(text), len(pattern)
            lps = [0] * m
            j = 0
            
            for i in range(1, m):
                while j > 0 and pattern[i] != pattern[j]:
                    j = lps[j - 1]
                if pattern[i] == pattern[j]:
                    j += 1
                    lps[i] = j
            
            res, j = [], 0
            for i in range(n):
                while j > 0 and text[i] != pattern[j]:
                    j = lps[j - 1]
                if text[i] == pattern[j]:
                    j += 1
                if j == m:
                    res.append(i - m + 1)
                    j = lps[j - 1]
            return res

        
        a_indices = kmp_search(s, a)
        b_indices = kmp_search(s, b)

        result = []
        j = 0

        
        for i in a_indices:
            while j < len(b_indices) and b_indices[j] < i - k:
                j += 1
            if j < len(b_indices) and abs(b_indices[j] - i) <= k:
                result.append(i)
        
        return result