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
            while cur.next and cur.next.val == cur.val:
                cur=cur.next
    
            if changing.next != cur:
                changing.next = cur.next
            else:
                changing=cur
        return node.next
                
            