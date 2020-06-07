class Solution:
    # opt[x][y] is the minimum sum can get from position (0,0) to position (x,y)
    # opt[m][n] = min(opt[x-1][y], opt[x][y-1]) + grid[x][y]
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n= len(grid[0])
        self.opt=[[None]*n for i in range(m)]
        self.opt[0][0]=grid[0][0]
        for i in range(1,m):
            self.opt[i][0] = self.opt[i-1][0] + grid[i][0]
        for i in range(1,n):
            self.opt[0][i] = self.opt[0][i-1] + grid[0][i]
        return self.helper(m-1,n-1,grid)
            
        
    def helper(self,x,y,grid):
        if self.opt[x][y] is not None:
            return self.opt[x][y]
        self.opt[x][y]= min(self.helper(x-1,y,grid),self.helper(x,y-1,grid))+grid[x][y]
        return self.opt[x][y]
            
        