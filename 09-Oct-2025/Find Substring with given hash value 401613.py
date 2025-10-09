# Problem: Find Substring with given hash value - https://leetcode.com/problems/find-substring-with-given-hash-value/description/

class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        n = len(s)
        p_pow = 1
        hash_val = 0
        result_index = 0
        
        p_k = pow(power, k, modulo)
        
        for i in range(n - 1, -1, -1):
            
            val = ord(s[i]) - 96           
            hash_val = (hash_val * power + val) % modulo
            
            if i + k < n:
                rem_val = (ord(s[i + k]) - 96) * p_k % modulo
                hash_val = (hash_val - rem_val + modulo) % modulo
            
            if hash_val == hashValue:
                result_index = i
        
        return s[result_index: result_index + k]