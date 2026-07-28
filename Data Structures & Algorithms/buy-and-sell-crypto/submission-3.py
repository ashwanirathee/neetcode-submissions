class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        p = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                pc = prices[r] - prices[l]
                p = max(p, pc)
            else:
                l = r
            r += 1
        return p