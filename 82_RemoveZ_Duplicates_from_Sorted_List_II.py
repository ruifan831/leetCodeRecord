# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        node = changing= ListNode()
        node.next = head
        pre_num=None
        while changing.next:
            cur = changing.next
            # let the cur pointer point to the last node for all nodes has the same val.
            while cur.next and cur.next.val == cur.val:
                cur=cur.next
            # since if the next node does not have duplicates, then the cur pointer should point to the same node of changing.next.
            # if not the same, then we know the next node has duplicate value.
            # Then the changing.next will point to the cur.next
            if changing.next != cur:
                changing.next = cur.next
            else:
                changing=cur
        return node.next
                
            