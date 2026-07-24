class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        def dfs(i, looted):
            if i >= n:
                return 0
            
            if i == n-1 and looted:
                return 0

            if (i,looted) in memo:
                return memo[(i,looted)]
                
            r1 = dfs(i+2, looted) + nums[i]# skip
            r2 = dfs(i+1, looted)
            memo[(i,looted)] = max(r1, r2)
            return memo[(i,looted)]

        return max(dfs(1, 0), dfs(2, 1) + nums[0])