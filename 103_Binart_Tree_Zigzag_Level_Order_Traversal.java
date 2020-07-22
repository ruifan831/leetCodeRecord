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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        Boolean reverse = false;
        if (root == null) return res;
        Stack<TreeNode> cur = new Stack<TreeNode>();
        Stack<TreeNode> next = new Stack<TreeNode>();
        List<Integer> temp = new ArrayList<Integer>();
        cur.push(root);
        while (!cur.empty()){
            TreeNode cur_node = cur.pop();
            temp.add(cur_node.val);
            if (reverse){
                if (cur_node.right != null) next.push(cur_node.right);
                if (cur_node.left != null) next.push(cur_node.left);
            } else {
                if (cur_node.left != null) next.push(cur_node.left);
                if (cur_node.right != null) next.push(cur_node.right);
            }
            if (cur.empty()){
                List<Integer> t = new ArrayList<Integer>(temp);
                res.add(t);
                temp.clear();
                reverse = !reverse;
                cur = (Stack<TreeNode>)next.clone();
                next.clear();
            }
            
        }
        return res;
        
        
        
    }
}