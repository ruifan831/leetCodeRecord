class Solution:
    def jump(self, nums: List[int]) -> int:
        opt = [None]*len(nums)
        opt[len(nums)-1] = 0
        def helper(i):
            if opt[i] is not None:
                return opt[i]
            else:
                opt[i] = float("inf")
                for k in range(i+1,min(nums[i]+i+1,len(nums))):
                    opt[i] = min(opt[i],helper(k)+1)
            return opt[i]
        return helper(0)
        


# OPT[i] is the minimum step need to jump to end of the array at position i.