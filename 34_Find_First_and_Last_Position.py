class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        s = self.find_first(nums,target)
        print(s)
        if s < 0 or s>=len(nums) or nums[s] != target:
            return [-1,-1]
        else:
            return [s,self.find_last(nums,target)]
    
    def find_first(self,nums,target):
        if nums:
            s,e = 0,len(nums)-1
            while s<=e:
                m = (s+e)//2
                if nums[m] >= target:
                    e = m-1
                else:
                    s = m+1
            return s
        else:
            return -1
    
    def find_last(self,nums,target):
        s,e = 0,len(nums)-1
        while s<=e:
            m = (s+e)//2
            if nums[m] > target:
                e = m-1
            else:
                s = m+1
        return e
    
            
        