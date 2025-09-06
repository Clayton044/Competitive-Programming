# Problem: Sum of Two Integers - https://leetcode.com/problems/sum-of-two-integers/description/

class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        while b != 0:
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK
        return a if a <= 0x7FFFFFFF else ~(a ^ MASK)