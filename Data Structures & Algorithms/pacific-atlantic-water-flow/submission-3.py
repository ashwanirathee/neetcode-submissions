class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pac = set()
        atl = set()

        def range_check(i, j):
            if i not in range(rows) or j not in range(cols):
                return False
            return True

        n = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        def dfs(i, j, s):
            if (i, j) in s:
                return
            s.add((i, j))

            for p, q in n:
                ni, nj = i + p, j + q
                if range_check(ni, nj) and heights[ni][nj] >= heights[i][j]:
                    dfs(ni, nj, s)

        for i in range(cols):
            dfs(0, i, pac)
            dfs(rows - 1, i, atl)

        for i in range(rows):
            dfs(i, 0, pac)
            dfs(i, cols - 1, atl)

        output = []
        for i in range(rows):
            for j in range(cols):
                if (i, j) in pac and (i, j) in atl:
                    output.append([i, j])
        return output
