class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bp = float("inf")
        p = 0

        for j in prices:
            bp = min(bp, j)
            p = max(p, j - bp)
        return p