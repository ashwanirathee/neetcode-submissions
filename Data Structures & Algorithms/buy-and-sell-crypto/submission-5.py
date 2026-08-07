class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        inf = float("inf")
        buy_price = inf
        max_profit = -inf

        for curr_price in prices:
            buy_price = min(buy_price, curr_price)
            max_profit = max(max_profit, curr_price - buy_price)
        return max_profit