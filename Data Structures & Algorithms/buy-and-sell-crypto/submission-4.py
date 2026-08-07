class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bp = float("inf")
        mp = -float("inf")

        for i in prices:
            bp = min(bp, i)
            mp = max(mp, i - bp)
        return mp