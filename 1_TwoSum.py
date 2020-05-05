class Solution:
    def twoSum(self, nums, target):
        temp=dict()
        for i,j in enumerate(nums):
            current_needs=target-j
            exist=temp.get(current_needs,None)
            if exist:
                return (i,temp[current_needs])
            else:
                temp[j]=i