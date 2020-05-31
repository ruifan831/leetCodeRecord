class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = list()
        path = []
        self.dfs(target,candidates,0,result,path)
        return result
        
        
    
    def dfs(self,target,candidates,index,result,path):
        if target <= 0:
            if target == 0:
                result.append(path[:])
            return
        if index < len(candidates):
            cur_value = candidates[index]
            path.append(cur_value)
            self.dfs(target-cur_value,candidates,index,result,path)
            path.pop()
            self.dfs(target,candidates,index+1,result,path)
        return
                