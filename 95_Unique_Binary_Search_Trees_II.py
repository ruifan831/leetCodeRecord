# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def generateTrees(self, n):
        return self.constructBST(1,n)
    def constructBST(self,s,e):
        result=[]
        if s>e:
            return result
        for i in range(s,e+1):
            left=self.constructBST(s,i-1)
            right=self.constructBST(i+1,e)
            
            if len(left)==0 and len(right)==0:
                root=TreeNode(i)
                result.append(root)
            elif len(left) == 0:
                for r in right:
                    root=TreeNode(i)
                    root.right=r
                    result.append(root)
            elif len(right) == 0:
                for l in left:
                    root=TreeNode(i)
                    root.left=l
                    result.append(root)
            else:
                for l in left:
                    for r in right:
                        root=TreeNode(i)
                        root.left=l
                        root.right=r
                        result.append(root)
        return result
