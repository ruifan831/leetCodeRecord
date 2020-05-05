class Solution:
    def threeSum(self, nums):
        result = []
        nums = sorted(nums) #Time Complexity O(NlogN)
        for i in range(len(nums)-2):
            if nums[i] > 0: #O(1)
                break
            if i>0 and nums[i]==nums[i-1]: # O(1)
                continue
            l= i+1  # O(1)
            r= len(nums)-1  # O(1)
            
            while l<r: # O(N)

                temp_result = nums[i]+nums[l]+nums[r] 
                if temp_result>0:
                    r -= 1
                elif temp_result <0:
                    l += 1
                else:
                    result.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l] == nums[l+1]:
                        l +=1
                    while l<r and nums[r] == nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
        return result