# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return head
        # k might greater than length of head.
        # it is a waste to keep rotate the head if the linked list has been rotated for a full round.
        # so we wanna tinker k so that we dont need to rotate over and over, but the result is still the same.
        # Since we know every length of head times, the linked list is restore to the original list.
        # Hence we change K to K%(length of head)
        node = ListNode(0,head)
        length = 0
        while head:
            head=head.next
            length+=1
        k = k%length
        head= node.next
        # only rotate the list for one step, and keep rotate until k is equal to 0.
        while k>0:
            node = changing = ListNode()
            node.next = head
            while head.next:
                changing= changing.next
                head=head.next
            changing.next = head.next
            head.next = node.next
            k-=1
            
        return head
            
            
        