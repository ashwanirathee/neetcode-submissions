class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        n = len(nums)
        def dfs(i, prev):
            if i == n:
                return 0

            pkey = (i,prev)
            if pkey in memo:
                return memo[pkey]
                
            skip = dfs(i+1, prev)

            rob = 0
            if prev == -1 or nums[i] > nums[prev]:
                rob = dfs(i+1, i) + 1

            memo[pkey] = max(skip,rob)
            return memo[pkey]
            
        return dfs(0, -1)