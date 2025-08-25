# Problem: Single Number - https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for char in nums:
            if nums.count(char)==1:
                return char
                