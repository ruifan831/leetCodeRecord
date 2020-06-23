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
    private int res= 0;
    public int longestUnivaluePath(TreeNode root) {
        helper(root);
        return res;
    }
    
    private int helper(TreeNode node){
        if (node == null){
            return 0;
        }
        int left = helper(node.left);
        int right = helper(node.right);
        int leftLen = 0, rightLen = 0;
        if (node.left != null && node.left.val ==node.val){
            leftLen = left +1;
        }
        if (node.right != null && node.right.val ==node.val){
            rightLen = right +1;
        }
        res = Math.max(res, leftLen+rightLen);
        return Math.max(leftLen,rightLen);
        
    }
}