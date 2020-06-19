# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        self.default=collections.defaultdict(list)
        self.bfs(root,0)
        return list(reversed(self.default.values()))
        
        
        
    def bfs(self,node,level):
        if node is None:
            return
        self.default[level].append(node.val)
        self.bfs(node.left,level+1)
        self.bfs(node.right,level+1)
        return
        
        