# Problem: Single Number II - https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in range(32): 
            bit_sum = 0
            mask = 1 << i
            for num in nums:
                if num & mask:
                    bit_sum += 1
            if bit_sum % 3 != 0:
                result |= mask
       
       
        if result & (1 << 31):
            result -= (1 << 32)

        return result