class Solution:
    def longestPalindrome(self, s: str) -> str:
        memo = {}
        def dfs(left, right):
            if left > right:
                return (0,0)

            pkey = (left, right)
            if pkey in memo:
                return memo[pkey]

            current = s[left:right+1]
            if current == current[::-1]:
                memo[pkey] = (left, right)
                return (left, right)

            l1, r1 = dfs(left+1, right)
            l2, r2 = dfs(left, right-1)
            if r1-l1 > r2-l2:
                memo[pkey] = (l1, r1)
                return memo[pkey]
            
            memo[pkey] = (l2, r2)
            return memo[pkey]
        
        l, r = dfs(0, len(s)-1)
        return s[l:r+1]