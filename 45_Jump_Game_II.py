class Solution:
    def jump(self, nums: List[int]) -> int:
        furthest_at_current_step=0
        furthest = 0
        step = 0
        for i in range(len(nums)-1):
            furthest = max(furthest,i+nums[i])
            # when the current index reaches the furthest index that the current number of step can reach.
            # We know that we have to take one more step to find further index can be reach.
            # increment step by one and update furthest_at_current_step to the furthest can be reach while iterating the index.
            if i == furthest_at_current_step:
                step +=1
                furthest_at_current_step = furthest
        return step

# Dynamic Solution, did not pass the last case.
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