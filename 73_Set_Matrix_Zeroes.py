class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        rowToBeZero=set()
        colToBeZero=set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rowToBeZero.add(i)
                    colToBeZero.add(j)
        for i in range(m):
            for j in range(n):
                if j in colToBeZero or i in rowToBeZero:
                    matrix[i][j]=0
