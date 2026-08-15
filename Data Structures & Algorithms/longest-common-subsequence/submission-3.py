class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        s1 = ""
        s2 = ""
        memo = {}
        def dfs(i, j, s1, s2):
            pkey = (i, j, s1, s2)
            if pkey in memo:
                return memo[pkey]

            if i == len(text1) or j == len(text2):
                if s1 == s2:
                    return len(s1)
                return 0

            r1 = r2 = r3 = 0

            if text1[i] == text2[j]:
                s1 = s1 + text1[i]
                s2 = s2 + text2[j]
                r1 = dfs(i + 1, j + 1, s1, s2)

            else:
                r2 = dfs(i + 1, j, s1, s2)
                r3 = dfs(i, j + 1, s1, s2)

            memo[pkey] = max(r1, r2, r3)
            return memo[pkey]

        return dfs(0, 0, s1, s2)