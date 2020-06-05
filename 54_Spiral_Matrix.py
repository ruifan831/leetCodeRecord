class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res= []
        if len(matrix) == 0:
            return res
        m,n = len(matrix),len(matrix[0])
        x,y = 0,0
        # move is the pattern how the next move will be
        move ={
            0: [0,1],
            1: [1,0],
            2: [0,-1],
            3: [-1,0]
        }
        key = 0
        for i in range(m*n):
            res.append(matrix[x][y])
            matrix[x][y] = False
            temp_x = x+move[key][0]
            temp_y = y+move[key][1]
            # everytime time if the next move will cause the x,y out of boundary 
            # or encounter a number has seen before change the move pattern
            if temp_x==m or temp_y==n or matrix[temp_x][temp_y] == False:
                key = (key+1)%4
            x+=move[key][0]
            y+=move[key][1]
            
        return res
            
                