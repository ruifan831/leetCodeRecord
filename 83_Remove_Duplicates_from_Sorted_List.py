# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        node= slow = ListNode(0.1,next=head)
        while head:
            if head.val == slow.val:
                head=head.next
            else:
                slow.next=head
                head=head.next
                slow=slow.next
        slow.next=head
        return node.next
        