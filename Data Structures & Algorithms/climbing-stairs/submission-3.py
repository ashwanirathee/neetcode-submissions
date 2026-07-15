class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1]*n
        def dfs(i):
            if i == n:
                return 1
            if i > n:
                return 0
            # print(i+1)
            if cache[i] != -1:
                return cache[i]
            cache[i] = dfs(i+1) + dfs(i+2)
            # depending on how you write you end up list out of range 
            # cases if not careful
            return cache[i]

        return dfs(0)