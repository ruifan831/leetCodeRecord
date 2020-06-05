class Solution:
    res=0
    def totalNQueens(self, n: int) -> int:
        
        diag_used = [False]*(2*n-1)
        diag_used_2 = [False]*(2*n-1)
        vertical = [False]*(2*n-1)
        board = ["."*n]*n
        self.dfs(0,board,n,diag_used,diag_used_2,vertical)
        return self.res
    
    def dfs(self,x,board,n,diag_used,diag_used_2,vertical):
        if x == n:
            self.res+=1
            return
        for y in range(n):
            d1 = x+y
            d2 = x-y+n-1
            if diag_used[d1] or diag_used_2[d2] or vertical[y]:
                continue
        
            prev = board[x]
            board[x] = board[x][:y] + "Q"+board[x][y+1:]
            diag_used[d1] =True
            diag_used_2[d2] = True
            vertical[y] = True
            self.dfs(x+1,board,n,diag_used,diag_used_2,vertical)
            board[x] = prev
            diag_used[d1] =False
            diag_used_2[d2] = False
            vertical[y] = False
            
        return
class Solution2:
    def totalNQueens(self, n: int) -> int:
        res = []
        diag_used = [False]*(2*n-1)
        diag_used_2 = [False]*(2*n-1)
        vertical = [False]*(2*n-1)
        board = ["."*n]*n
        self.dfs(0,board,res,n,diag_used,diag_used_2,vertical)
        return len(res)
    
    def dfs(self,x,board,res,n,diag_used,diag_used_2,vertical):
        if x == n:
            res.append(board[:])
            return
        for y in range(n):
            d1 = x+y
            d2 = x-y+n-1
            if diag_used[d1] or diag_used_2[d2] or vertical[y]:
                continue
        
            prev = board[x]
            board[x] = board[x][:y] + "Q"+board[x][y+1:]
            diag_used[d1] =True
            diag_used_2[d2] = True
            vertical[y] = True
            self.dfs(x+1,board,res,n,diag_used,diag_used_2,vertical)
            board[x] = prev
            diag_used[d1] =False
            diag_used_2[d2] = False
            vertical[y] = False
            
        return