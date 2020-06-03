class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        path = []
        used = [False]*len(nums)
        self.dfs(result,path,nums,used)
        return result
    

    # Same idea as 46_Permuation.py
    # However, everytime the dfs tree expand to the next level, need to consider if the current number is the same as previous num in the same level.
    def dfs(self,res,path,nums,used):
        if len(path) == len(nums):
            res.append(path[:])
            return
        i=0
        while i < len(nums):
            if not used[i]:
                # consider the situation when the first dfs path has been explored and starting the new explore path.
                # skip the next number in the same level of the dfs tree if the number is equal to the previous one and the previous one has not been used.
                if i>=1 and nums[i-1] == nums[i] and not used[i-1]:
                    i+=1
                    continue
                path.append(nums[i])
                used[i] = True
                self.dfs(res,path,nums,used)
                path.pop()
                used[i] = False
            i+=1
        return

class Solution_2:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
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
                if i>0 and nums[i-1] == num and not used[i-1]:
                    continue
                used[i] = True
                path.append(num)
                self.dfs(res,path,nums,used)
                path.pop()
                used[i] = False
        return
    
