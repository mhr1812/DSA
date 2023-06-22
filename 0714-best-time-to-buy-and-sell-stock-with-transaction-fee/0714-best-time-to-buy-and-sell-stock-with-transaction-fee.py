class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy,sell = -prices[0],0
        for e in prices:
            buy = max(buy,sell-e)
            sell = max(sell,buy+e-fee)
        return sell