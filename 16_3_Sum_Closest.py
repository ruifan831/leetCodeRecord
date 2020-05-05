class Solution:
    def threeSumClosest(self, nums, target) -> int:
        result = float('inf')
        nums = sorted(nums)
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l= i+1
            r= len(nums)-1
            while l<r:
                temp_result = nums[i]+nums[l]+nums[r]-target
                if abs(temp_result)< abs(result-target):
                    result = temp_result +target
                if temp_result>0:
                    r -= 1
                elif temp_result <0:
                    l += 1
                else:
                    result = target
                    return result
        return result
        