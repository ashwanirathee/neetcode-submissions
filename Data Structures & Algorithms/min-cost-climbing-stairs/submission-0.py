class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cache = [-1] * n

        def dfs(i):
            print(i)
            if i >= n:
                return 0
            if cache[i] != -1:
                return cache[i]
            cache[i] = min(dfs(i+1), dfs(i+2)) + cost[i]
            return cache[i]

        return min(dfs(0), dfs(1))