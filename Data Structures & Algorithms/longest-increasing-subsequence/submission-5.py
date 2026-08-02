class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}

        def dfs(i, previous_index):
            if i == n:
                return 0

            key = (i, previous_index)

            if key in memo:
                return memo[key]

            # Skip nums[i]
            skip = dfs(i + 1, previous_index)

            # Take nums[i], if it is increasing
            take = 0

            if previous_index == -1 or nums[i] > nums[previous_index]:
                take = 1 + dfs(i + 1, i)

            memo[key] = max(take, skip)
            return memo[key]

        return dfs(0, -1)