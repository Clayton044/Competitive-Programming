# Problem: Decode XORed Permutation - https://leetcode.com/problems/decode-xored-permutation/description/?envType=problem-list-v2&envId=bit-manipulation

class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1
        total = 0
        for i in range(1, n + 1):
            total ^= i
        suffix = 0
        for i in range(1, n, 2):
            suffix ^= encoded[i]
        first = total ^ suffix
        perm = [first]
        for i in range(n - 1):
            perm.append(perm[-1] ^ encoded[i])
        return perm