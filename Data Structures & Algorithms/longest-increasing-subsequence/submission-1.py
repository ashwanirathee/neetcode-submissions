class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        n = len(nums)
        def dfs(i, prev):
            if i == n:
                return 0
            if (i,prev) in memo:
                return memo[(i,prev)]
            skip = dfs(i+1, prev)

            rob = 0
            if prev == -1 or nums[i] > nums[prev]:
                rob = dfs(i+1, i) + 1
            memo[(i,prev)] = max(skip,rob)
            return memo[(i,prev)]
            
        return dfs(0, -1)