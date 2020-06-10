class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1,p2=0,len(nums)
        while p1<p2:
            for i in range(p1+1,p2):
                if nums[p1]>nums[i]:
                    nums[p1],nums[i]=nums[i],nums[p1]
            p1+=1
                
                
        