class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        def dfs(i, looted):
            if i >= n:
                return 0
            
            if i == n-1 and looted:
                return 0

            pkey = (i,looted)
            if pkey in memo:
                return memo[pkey]

            skip = dfs(i+1, looted)   
            rob = dfs(i+2, looted) + nums[i]# skip
            
            memo[pkey] = max(skip, rob)
            return memo[pkey]

        return max(dfs(1, False), dfs(2, True) + nums[0])