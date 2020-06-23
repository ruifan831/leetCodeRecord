/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private int res = 0;
    public int pathSum(TreeNode root, int sum) {
        if (root ==null) return 0;
        return dfs(root,sum)+pathSum(root.left,sum)+pathSum(root.right,sum);
        
        
    }
    
    private int dfs(TreeNode node,int target){
        int temp=0;
        if (node == null) return temp;
        if (node.val == target) temp+=1;
        temp += dfs(node.left,target-node.val);
        temp += dfs(node.right,target-node.val);
        return temp;
        
        
        
    }
}