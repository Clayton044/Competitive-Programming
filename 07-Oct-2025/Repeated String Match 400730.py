# Problem: Repeated String Match - https://leetcode.com/problems/repeated-string-match/description/

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        repeat = -(-len(b) // len(a)) 
        for i in range(repeat, repeat + 3): 
            if b in a * i:
                return i
        return -1