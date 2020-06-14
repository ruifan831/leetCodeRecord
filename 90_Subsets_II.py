class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.res=[[]]
        nums.sort()
        self.dfs(0,[],nums)
        return self.res
    def dfs(self,index,path,nums):
        if index==len(nums):
            return
        for i in range(index,len(nums)):
            if i> index and nums[i]==nums[i-1]:
                continue
            path.append(nums[i])
            self.res.append(path[:])
            self.dfs(i+1,path,nums)
            path.pop()
                