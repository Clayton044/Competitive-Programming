# Problem: Maximum Number of Consecutive Values You Can Make - https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/description/

class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        max_val = 0

        for coin in coins:
            if coin > max_val + 1:
                break
            max_val += coin

        return max_val + 1