# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # if head is None, return None
        if not head:
            return None
        mid = self.midNode(head)
        node = TreeNode(mid.val)
        # we need to find out if the mid pointer is point to the same node of head pointer
        # If the same, this means that the linked list only contains one node.
        # In this situation, just return node it self, this will prevent the infinite recursion.
        if head == mid:
            return node
        
        left=self.sortedListToBST(head)
        right=self.sortedListToBST(mid.next)
        node.left= left
        node.right=right
        return node
        
    # Using two pointer, one is slow and the other is fast
    # fast pointer moves two step and slow moves one step every time.
    # after fast pointer points to the last node, the slow pointer is pointing to the mid node.
    # Also create a pointer to store the node which is the node before slow pointer.
    # Because we would like to split the linked list into two linked list, and neither of these two linked list contain the mid node.
    # Hence, after iterated over the linked list, we need to set the node.next to None for the node that before_mid pointer points to.
    def midNode(self,node):
        before_mid=None
        fast = node
        slow = node
        while fast and fast.next:
            before_mid=slow
            fast=fast.next.next
            slow=slow.next
        if before_mid :
            before_mid.next= None
        return slow
    
