class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer_1=0
        pointer_2=1
        while pointer_2 <len(nums):
            if nums[pointer_1]==nums[pointer_2]:
                pointer_2+=1
            else:
                pointer_1 +=1
                nums[pointer_1]=nums[pointer_2]
                pointer_2 +=1
                
        return pointer_1+1