# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        elif len(nums)==1:
            return TreeNode(nums[0])
        s,e=0,len(nums)-1
        m = (s+e)//2
        print(s,m,e)
        
        left_list=nums[s:m]
        right_list=nums[m+1:]
        node=TreeNode(nums[m])
        node.left=self.sortedArrayToBST(left_list)
        node.right=self.sortedArrayToBST(right_list)
        return node
        
        