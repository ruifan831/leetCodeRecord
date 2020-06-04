class Solution_1:
    # 1. Enumerate position, find the possible number for position.
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        used = [False]*len(nums)
        self.dfs(result,path,nums,used)
        return result
    
    def dfs(self,res,path,nums,used):
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i,num in enumerate(nums):
            if not used[i]:
                path.append(num)
                used[i] = True
                self.dfs(res,path,nums,used)
                path.pop()
                used[i] = False
        return

class Solution_2:
    # 2. Enumerate nums, find possible position for num.
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = [-1]*len(nums)
        used = [False]*len(nums)
        self.dfs(0,result,path,nums,used)
        return result
    
    def dfs(self,cur_num,res,path,nums,used):
        if cur_num == len(nums):
            res.append(path[:])
            return
        for i in range(len(nums)):
            if not used[i]:
                path[i] = nums[cur_num]
                used[i] = True
                self.dfs(cur_num+1,res,path,nums,used)
                used[i] = False
        return
