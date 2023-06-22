class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy,sell = prices[0],0
        for e in prices:
            buy = min(buy,e)
            sell = max(sell,e-buy)
        return sell