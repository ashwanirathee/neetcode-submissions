class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = []

        for idx, value in enumerate(nums):
            no_rob = dp[idx - 1] if idx >= 1 else 0
            rob = (dp[idx - 2] if idx >= 2 else 0) + value

            max_score = max(no_rob, rob)
            dp.append(max_score)

        return dp[-1]
