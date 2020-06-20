# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        self.depth=0
        self.dfs(root,0)
        return self.depth
    
    def dfs(self,node,depth):
        if node is None:
            if depth>self.depth:
                self.depth=depth
            return
        self.dfs(node.left,depth+1)
        self.dfs(node.right,depth+1)
        return
        