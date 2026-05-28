class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice = prices[0]
        maxProfit = prices[0] - buyPrice

        for price in prices:
            # print(buyPrice, maxProfit)
            buyPrice = min(buyPrice, price)
            maxProfit = max(maxProfit, price-buyPrice)
        
        return maxProfit