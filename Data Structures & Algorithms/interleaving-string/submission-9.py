class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        def dfs(i, j, s, memo):
            if i == len(s1) and j == len(s2):
                return True

            pkey = (i, j)
            if pkey in memo:
                return memo[pkey]

            k = i + j
            r1 = r2 = False

            if i < len(s1) and s1[i] == s3[k]:
                r1 = dfs(i + 1, j, s, memo)

            if j < len(s2) and s2[j] == s3[k]:
                r2 = dfs(i, j + 1, s, memo)

            memo[pkey] = r1 or r2
            return memo[pkey]

        memo = {}
        i = 0
        j = 0
        return dfs(i, j, "", memo)
