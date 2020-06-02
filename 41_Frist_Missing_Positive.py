class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for index in range(len(nums)):
            # Keep swap the value at position nums[index]-1 and index if value at position nums[index]-1 is not equal to nums[index].
            # This can help to eliminate the problem causes by duplicate valid values in nums array at corresponding position. 
            while nums[index] > 0 and nums[index] <= len(nums) and nums[nums[index]-1] != nums[index]: # nums[index]-1 != index can cause the infinite while loop if duplicate valid values at corresponding position.
                    nums[nums[index]-1],nums[index] = nums[index],nums[nums[index]-1]
        for index, num in enumerate(nums):
            if num-1 != index:
                return index+1
        return len(nums)+1
        