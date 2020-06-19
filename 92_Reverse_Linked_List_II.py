# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        pre=None
        node=head
        
        while m>1:
            pre=head
            head=head.next
            m-=1
            n-=1
        p1=pre
        p2=head
        
        while n>0:
            nextNode = head.next
            head.next=pre
            pre=head
            head=nextNode
            n-=1
        p2.next=head
        if p1 is not None:
            p1.next=pre
        else:
            node=pre
        return node
        