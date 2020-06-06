class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[None]*n for i in range(n)]
        move= {
            0:[0,1],
            1:[1,0],
            2:[0,-1],
            3:[-1,0]
        }
        x,y=0,0
        direction = 0
        for i in range(1,n**2+1):
            matrix[x][y] = i
            next_x,next_y = x+move[direction][0],y+move[direction][1]
            if next_x==n or next_y==n or matrix[next_x][next_y] is not None:
                direction = (direction+1)%4
            x,y=x+move[direction][0],y+move[direction][1]
        return matrix