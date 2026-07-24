class Solution:
    def rob(self, nums: List[int]) -> int:
        m = 0
        n = len(nums)
        memo = {}
        def dfs(i, res):
            nonlocal m
            if i >= n:
                m = max(m, res)
                return

            if (i, res) in memo:
                return memo[(i, res)]
            memo[i+2, res+nums[i]] = dfs(i+2, res+nums[i]) # skip
            memo[i+1, res] = dfs(i+1, res)

        dfs(0, 0)
        return m