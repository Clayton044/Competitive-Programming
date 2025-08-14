# Problem: Best Time to Buy and Sell Stock III - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1 = buy2 = float('-inf')
        sell1 = sell2 = 0

        for stock in prices:
            buy1 = max(buy1, -stock)
            sell1 = max(sell1, stock + buy1)
            buy2 = max(buy2, sell1 - stock)
            sell2 = max(sell2, stock+buy2)

        return sell2