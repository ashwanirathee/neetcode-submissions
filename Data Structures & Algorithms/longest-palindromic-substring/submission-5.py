class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        memo = {}
        def dfs(left, right):
            nonlocal longest
            if left > right:
                return

            pkey = (left, right)
            current = s[left:right+1]
            if pkey in memo:
                return memo[pkey]

            if current == current[::-1]:
                memo[pkey] = current
                return current

            rleft = dfs(left+1, right)
            rright = dfs(left, right-1)
            if len(rleft) > len(rright):
                memo[pkey] = rleft
                return rleft
            
            memo[pkey] = rright
            return rright
        
        return dfs(0, len(s)-1)