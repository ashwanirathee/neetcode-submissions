class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        memo = {}
        def dfs(i):
            pkey = (i, len(stack))

            if pkey in memo:
                return memo[pkey]

            if i == len(s):
                memo[pkey] = len(stack) == 0
                return  memo[pkey]

            if s[i] == "(":
                stack.append("(")

                memo[pkey] = dfs(i + 1)

                # backtrack
                stack.pop()

                return memo[pkey]

            elif s[i] == ")":
                if not stack:
                    return False

                stack.pop()

                memo[pkey] = dfs(i + 1)

                # backtrack
                stack.append("(")

                return memo[pkey]

            else:
                # Case 1: * = '('
                stack.append("(")
                r1 = dfs(i + 1)
                stack.pop()

                # Case 2: * = empty
                r2 = dfs(i + 1)

                # Case 3: * = ')'
                r3 = False

                if stack:
                    stack.pop()

                    r3 = dfs(i + 1)

                    # backtrack
                    stack.append("(")

                memo[pkey] = r1 or r2 or r3
                return memo[pkey]

        return dfs(0)