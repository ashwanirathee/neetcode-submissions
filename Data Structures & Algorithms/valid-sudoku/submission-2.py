class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])
        res = dict()
        for i in range(rows):
            for j in range(cols):
                if board[i][j] != ".":
                    if f"row_{i}" not in res.keys():
                        res[f"row_{i}"] = set()
                    if f"col_{j}" not in res.keys():
                        res[f"col_{j}"] = set()

                    sec_i = i // 3
                    sec_j = j // 3
                    if f"sec_{sec_i}_{sec_j}" not in res.keys():
                        res[f"sec_{sec_i}_{sec_j}"] = set()

                    if board[i][j] not in res[f"row_{i}"]:
                        res[f"row_{i}"].add(board[i][j])
                    else:
                        return False

                    
                    if board[i][j] not in res[f"col_{j}"]:
                        res[f"col_{j}"].add(board[i][j])
                    else:
                        return False

                    if board[i][j] not in res[f"sec_{sec_i}_{sec_j}"]:
                        res[f"sec_{sec_i}_{sec_j}"].add(board[i][j])
                    else:
                        return False
        return True