class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        max_score = 0
        n = len(cardPoints)

        # @cache 
        memo = {}
        def dfs(l, r, rem, curr):
            print(l, r)
            nonlocal max_score
            if rem == 0:
                return 0
            pkey = (l, r, rem)
            if pkey in memo:
                return memo[pkey]

            take_left = cardPoints[l] + dfs(l+1, r, rem-1, curr + cardPoints[l])
            take_right = cardPoints[r] + dfs(l, r-1, rem-1, curr + cardPoints[r])
            memo[pkey] = max(take_left, take_right)
            return memo[pkey]


        curr = 0
        res = dfs(0, n-1, k, curr)
        return res

