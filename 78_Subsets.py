class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res=[[]]
        self.dfs(nums,0,[])
        return self.res
    
    def dfs(self,nums,index,path):
        if len(path)==len(nums):
            return
        for i in range(index,len(nums)):
            
            path.append(nums[i])
            self.res.append(path[:])
            self.dfs(nums,i+1,path)
            path.pop()