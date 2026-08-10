class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def dfs(i, j, idx):
            # matched whole word
            if idx == len(word):
                return True

            # out of bounds
            if i not in range(rows) or j not in range(cols):
                return False

            # current character doesn't match
            if board[i][j] != word[idx]:
                return False

            # mark visited
            temp = board[i][j]
            board[i][j] = "#"

            r1 = dfs(i + 1, j, idx + 1)
            r2 = dfs(i - 1, j, idx + 1)
            r3 = dfs(i, j + 1, idx + 1)
            r4 = dfs(i, j - 1, idx + 1)

            # backtrack
            board[i][j] = temp

            return r1 or r2 or r3 or r4

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True

        return False