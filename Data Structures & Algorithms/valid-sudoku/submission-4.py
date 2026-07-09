class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = 9
        cols = 9

        rows = [[] for i in range(9)]
        cols = [[] for i in range(9)]
        sub_boxes = [[] for i in range(9)]
        for i in range(9):
            for j in range(9):
                curr = board[i][j]
                if curr.isdigit():
                    print(curr, i, j)

                    if curr in rows[i]:
                        print("'return row")
                        return False
                    else:
                        rows[i].append(curr)

                    if curr in cols[j]:
                        print("'return col")
                        return False
                    else:
                        cols[j].append(curr)

                    num = int(i // 3) * 3  + int(j// 3)
                    print(curr, i, j, num)
                    if curr in sub_boxes[num]:
                        print("'return sub")
                        return False
                    else:
                        sub_boxes[num].append(curr)
        return True