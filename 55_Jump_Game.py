class Solution:
    def canJump(self, nums: List[int]) -> bool:
        j= len(nums)-1
        i = j
        # Iterate from last index to the first index of nums
        # Check if the farthest index can be reach at current position is greater than j.
        # Update j if True.
        while i>=0:
            if i + nums[i] >= j:
                j = i
            i-=1
        return j == 0

# Dynamic Programming Iterative
class Solution_2:
    def canJump(self, nums: List[int]) -> bool:
        opt=[None]*len(nums)
        opt[-1] =True
        i = len(nums) - 1
        while i>=0:
            for j in range(i,min(i+nums[i]+1,len(nums)))[::-1]:
                opt[i] = opt[j]
                if opt[i]:
                    break
            i-=1
        return opt[0]
# Dynamic Programing Recursive
class Solution_3:
    def canJump(self, nums: List[int]) -> bool:
        opt=[None]*len(nums)
        opt[-1] =True
    
        def helper(n):
            if opt[n]:
                return opt[n]
            opt[n] = False
            for i in range(n+1,n+nums[n]+1):
                opt[n] = opt[n] or helper(i)
                if opt[n]:
                    break
            return opt[n]
        helper(0)
        print(opt)
        return opt[0]
    