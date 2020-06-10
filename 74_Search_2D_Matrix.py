class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix)==0:
            return False
        row_len,col_len= len(matrix),len(matrix[0])
        s,e=0,row_len*col_len-1
        while s<=e:
            m=(s+e)//2
            row,col=divmod(m,col_len)
            if matrix[row][col]==target:
                return True
            elif matrix[row][col] > target:
                e=m-1
            else:
                s=m+1
        return False
        
        