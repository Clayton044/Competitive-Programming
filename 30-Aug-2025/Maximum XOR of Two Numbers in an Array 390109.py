# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        res = 0
        mask = 0
        for i in range(31, -1, -1):
            mask |= (1 << i)
            # print(mask)
            prefixes = {num & mask for num in nums}
            candidate = res | (1 << i)
            # print(candidate)
            if any(candidate ^ p in prefixes for p in prefixes):
                res = candidate
        return res