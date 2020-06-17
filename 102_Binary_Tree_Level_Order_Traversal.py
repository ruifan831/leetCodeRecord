# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        cur=[]
        next_level = []
        res=[]
        cur.append(root)
        while cur:   
            temp_result=[]
            for node in cur:
                temp_result.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            res.append(temp_result)
            cur=next_level[:]
            next_level.clear()
        return res
                    
