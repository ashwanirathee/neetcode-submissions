class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        n = len(s)
        d_set = {}
        res = 0

        while r < n:
            if s[r] in d_set and d_set[s[r]] >= l:
                l = d_set[s[r]] + 1

            d_set[s[r]] = r
            res = max(res, r - l + 1)
            r += 1

        return res