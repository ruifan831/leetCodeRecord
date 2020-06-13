class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.k=k
        self.n=n
        res = []
        self.dfs(res,0,[],0)
        return res
    
    def dfs(self,res,level,path,start):
        if level == self.k:
            res.append(path[:])
        for i in range(1+start,1+self.n):
            path.append(i)
            self.dfs(res,level+1,path,i)
            path.pop()