class Solution:
    # opt[m][n] is the number of unique path that can reach to position (m,n) from (0,0)
    # opt[m][n] = opt[m-1][n] + opt[m][n-1]
    # initialize opt[0][0] = 1
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n= len(obstacleGrid[0])
        self.opt=[[None]*n for i in range(m)]
        self.opt[0][0] = 1
        return self.helper(m-1,n-1,obstacleGrid)
    # Here x and y is possible to be less than 0.
    # When x or y is less than 0, we know it is out of boundary, hence, return 0
    # If the current position is obstacle, set opt[x][y] to 0.
    def helper(self,x,y,obstacleGrid):
        if x<0 or y<0:
            return 0
        if obstacleGrid[x][y] == 1:
            self.opt[x][y]=0
        if self.opt[x][y] is not None:
            return self.opt[x][y]
        cur = self.helper(x-1,y,obstacleGrid)+self.helper(x,y-1,obstacleGrid)
        self.opt[x][y] = cur
        return self.opt[x][y]