/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}
    
    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/

class Solution {
    public Node connect(Node root) {
        // if (root != null){
        //     System.out.println(root.val);
        // } else {
        //     System.out.println("Null");
        // }
        if (root == null || (root.left == null && root.right == null)) return root;
        if (root.left!=null && root.right!=null){
            root.left.next=root.right;
            root.right.next = getNext(root);
        } else if(root.right == null){
            root.left.next = getNext(root);
        } else {
            root.right.next = getNext(root);  
        }
        connect(root.right);
        connect(root.left);
        
        return root;
    }
    
    private Node getNext(Node node){
        Node next = node.next;
        while (next != null){
            if (next.left != null) return next.left;
            if (next.right != null) return next.right;
            next = next.next;
        }
        return null;
    }
    
    
}