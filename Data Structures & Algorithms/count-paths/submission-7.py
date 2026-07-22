class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def solve(i, j, m, n):
            if i not in range(m) or j not in range(n):
                return 0

            if i == m - 1 and j == n - 1:
                return 1

            if (i, j) in memo:
                return memo[(i, j)]

            a = solve(i + 1, j, m, n)
            b = solve(i, j + 1, m, n)

            memo[(i, j)] = a + b
            return a + b

        count = solve(0, 0, m, n)
        return count
