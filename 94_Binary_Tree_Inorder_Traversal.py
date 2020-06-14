# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.res=[]
        self.helper(root)
        return self.res
    def helper(self,node):
        if node is None:
            return
        self.helper(node.left)
        self.res.append(node.val)
        self.helper(node.right)

# Iterative

class Solution_2:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res=[]
        stack=[]
        while root is not None or stack:
            while root is not None:
                stack.append(root)
                root=root.left
            root = stack.pop()
            res.append(root.val)
            root=root.right
        return res 
        