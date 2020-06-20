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
    public void flatten_Recursive(TreeNode root) {
        if (root == null) return ;
        
        flatten_Recursive(root.left);
        flatten_Recursive(root.right);
        // After flatten(root.left) and flatten(right)
        // We can sure that root.left and root.right are already flattened to linked list 
        if (root.left !=null && root.right == null){
            root.right=root.left;
            root.left = null;
        }
        // we wanna find the end TreeNode of the left flattened tree and assign its right node as the begining TreeNode of the right flattened tree.
        // Then update the root.right as root.left.
        if (root.left !=null && root.right !=null){
            TreeNode leftEnd = root.left;
            while (leftEnd.right != null){
                leftEnd = leftEnd.right;
            }
            leftEnd.right = root.right;
            root.right=root.left;
            root.left=null;
        }  
    }
    public void flatten(TreeNode root) {
        if (root == null) return ;
        Stack<TreeNode> stack = new Stack();
        stack.push(root);
        while (!stack.isEmpty()){
            TreeNode cur = stack.pop();
            if (cur.right!=null){
                stack.push(cur.right);
            }
            if (cur.left!=null){
                stack.push(cur.left);
            }
            if (!stack.isEmpty()){
                cur.right=stack.peek();
            }
            cur.left = null;
        }
        
        
    }
}