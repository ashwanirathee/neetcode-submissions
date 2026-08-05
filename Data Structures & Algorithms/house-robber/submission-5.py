class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i):
            if i >= len(nums):
                return 0
            pkey = (i)
            if pkey in memo:
                return memo[pkey]

            skip = dfs(i+1)
            take = dfs(i+2) + nums[i]
            memo[pkey] = max(skip, take)
            return memo[pkey]
        res = dfs(0)
        return res