class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # construct bit map for each row, column and box.
        row = [0]*9
        col = [0]*9
        box = [0]*9
        # for each value in the board, check if it has been occured in corresponding row, column or boxes by using bitwise AND Operation
        for i in range(9):
            for j in range(9):
                cur_val = board[i][j]
                if cur_val == ".":
                    continue
                cur_val = 1 << (ord(cur_val) - ord("1"))
                print(cur_val)
                if cur_val & row[i] or cur_val & col[j] or cur_val & box[3*(i//3) + j//3]:
                    return False
                row[i] |= cur_val
                col[j] |= cur_val
                box[3*(i//3) + j//3] |= cur_val
        return True