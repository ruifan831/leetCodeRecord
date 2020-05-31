class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                cur = 1 << (ord(board[i][j]) - ord("1"))
                rows[i] |= cur
                cols[j] |= cur
                boxes[3*(i//3) + j//3] |= cur
        self.fill(0,0,board,rows,cols,boxes)
    
    def fill(self,x,y,board,rows,cols,boxes):
        if y == 9:
            x += 1
            y = 0
        if x == 9:
            return True
        if board[x][y] == ".":
            for i in range(9):
                fill_num = 1 << i
                if not (rows[x] & fill_num or cols[y] & fill_num or boxes[3*(x//3)+y//3] & fill_num):
                    rows[x] |= fill_num
                    cols[y] |= fill_num
                    boxes[3*(x//3)+y//3] |= fill_num
                    board[x][y] = str(i+1)
                    if self.fill(x,y+1,board,rows,cols,boxes):
                        return True
                    rows[x] -= fill_num
                    cols[y] -= fill_num
                    boxes[3*(x//3)+y//3] -= fill_num
                    board[x][y] = "."
        else:
            if self.fill(x,y+1,board,rows,cols,boxes):
                return True
                    
                    
        return False