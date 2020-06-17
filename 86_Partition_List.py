# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        p1=p1_change = ListNode()
        p2=p2_change=ListNode()
        while head:
            if head.val<x:
                p1_change.next=head
                p1_change=p1_change.next
            else:
                p2_change.next=head
                p2_change=p2_change.next
            head=head.next
        p2_change.next=None
        p1_change.next=p2.next
        return p1.next
            