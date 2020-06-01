class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        print(candidates)
        self.dfs(candidates,target,result,[],0)
        return result
    
    
    def dfs(self,candidates,target,result,path,index):
        if target <= 0:
            if target ==0:
                result.append(path[:])
            return
        if index< len(candidates):
            path.append(candidates[index])
            self.dfs(candidates,target-candidates[index],result,path,index+1)
            path.pop()
            while index+1<len(candidates):
                if candidates[index] == candidates[index+1]:
                    index +=1
                else:
                    break
            self.dfs(candidates,target,result,path,index+1)
            
        return
            
        
        