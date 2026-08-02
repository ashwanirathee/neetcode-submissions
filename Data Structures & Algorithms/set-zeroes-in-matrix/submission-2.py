class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        rows_set = [1]*rows
        cols_set = [1]*cols
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    rows_set[i] = 0
                    cols_set[j] = 0


        for i in range(rows):
            for j in range(cols):
                if rows_set[i]==0 or cols_set[j]==0:
                    matrix[i][j] =0
        # return matrix