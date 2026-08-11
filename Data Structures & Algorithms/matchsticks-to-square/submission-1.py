class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        memo = {}
        def dfs(i,s1,s2,s3,s4):
            if i == len(matchsticks):
                if s1 == s2 == s3 == s4:
                    return True
                else:
                    return False

            pkey = (i,s1,s2,s3,s4)
            if pkey in memo:
                return memo[pkey]

            r1 = dfs(i+1, s1+matchsticks[i],s2,s3,s4)
            r2 = dfs(i+1, s1, s2+matchsticks[i],s3,s4)
            r3 = dfs(i+1, s1,s2,s3+matchsticks[i],s4)
            r4 = dfs(i+1, s1,s2,s3,s4+matchsticks[i])
            memo[pkey] = r1 or r2 or r3 or r4
            return memo[pkey]

        return dfs(0, 0,0,0,0)
