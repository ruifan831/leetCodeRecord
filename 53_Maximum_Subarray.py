class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        opt = [-1*float("inf")]*len(nums)
        for i,num in enumerate(nums):
            if i == 0:
                opt[i] = num
            else:
                opt[i] = max(num,num+opt[i-1])          
        return max(opt)
            