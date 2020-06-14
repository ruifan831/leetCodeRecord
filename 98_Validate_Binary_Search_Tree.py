# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(-float("inf"),float("inf"),root)
    
    def helper(self,min_,max_,node):
        if node is None:
            return True
        if min_ < node.val < max_:
            return self.helper(min_,node.val,node.left) and self.helper(node.val,max_,node.right)
        else:
            return False