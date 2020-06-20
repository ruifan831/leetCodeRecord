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
    private List<List<Integer>> res = new ArrayList<List<Integer>>();
    public List<List<Integer>> pathSum(TreeNode root, int sum) {
        if (root == null){
            return res;
        }
        Stack<Integer> path = new Stack<Integer>(); 
        dfs(root,sum,path);
        return res;
    }
    
    private void dfs(TreeNode node,int target, Stack<Integer> path){
        path.push(node.val);
        if (node.left== null && node.right==null){
            if (target==node.val){
                res.add(new ArrayList<Integer>(path));
            }
        }
        
        if (node.left != null){
            dfs(node.left,target-node.val,path);
        }
        if (node.right != null){
            dfs(node.right,target-node.val,path);
        }
        path.pop();
    }
    
}
