class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        total = 0
        n = len(coins)
        memo = {}
        min_count = float("inf")
        def dfs(i, res, coin_count):
            # print(i, res)
            nonlocal total, min_count
            if i == n or res >= amount:
                if res == amount:
                    total += 1
                    min_count = min(min_count, coin_count)
                    return 1
                return 0
            
            pkey = (i, res, coin_count)
            if pkey in memo:
                return memo[pkey]

            r1 = dfs(i, res + coins[i], coin_count+1)
            r2 = dfs(i+1, res, coin_count)

            memo[pkey] = r1 + r2
            return memo[pkey]

        # idx, total_til_now
        memo[(0,0,0)] = dfs(0, 0, 0)
        return -1 if min_count == float("inf") else min_count