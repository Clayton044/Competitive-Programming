# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        hold, rest, sold = -prices[0], 0, 0
        for p in prices[1:]:
            hold, rest, sold = max(hold, rest - p), max(rest, sold), hold + p
        return max(rest, sold)