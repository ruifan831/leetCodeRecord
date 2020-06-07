class Solution:
    # opt[m][n] is the number of unique path that can reach to position (m,n) from (0,0)
    # opt[m][n] = opt[m-1][n] + opt[m][n-1]
    # initialize opt[x][0] = 1 (x = 0 to m-1), opt[0][y] = 1 (y = 0 to n-1)
    def uniquePaths(self, m: int, n: int) -> int:
        self.opt=[[None]*n for i in range(m)]
        for i in range(m):
            self.opt[i][0] = 1
        for i in range(n):
            self.opt[0][i] = 1
        return self.helper(m-1,n-1)
    
    def helper(self,x,y):     
        if self.opt[x][y] is not None:
            return self.opt[x][y]
        cur = self.helper(x-1,y)+self.helper(x,y-1)
        self.opt[x][y] = cur
        return self.opt[x][y]