class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        used=[[False]*len(board[0]) for _ in board]
        m,n=len(board),len(board[0])
        for i in range(m):
            for j in range(n):
                if self.dfs(used,0,i,j,word,m,n,board):
                    return True
        return False
        
        
    
    def dfs(self,used,index,row,col,word,m,n,board):
        if not (0<=row < m and 0 <= col < n):
            return False
        if board[row][col] != word[index] or used[row][col]:
            return False
        if index==len(word)-1:
            return True
        result=False
        used[row][col] = True
        for i,j in [(row+1,col),(row-1,col),(row,col+1),(row,col-1)]:
            result = result or self.dfs(used,index+1,i,j,word,m,n,board)
        used[row][col] = False
        return result