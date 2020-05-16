# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #   Recursive
    # def swapPairs(self, head: ListNode) -> ListNode:
    #     if head and head.next:
    #         temp = head.next
    #         head.next=self.swapPairs(temp.next)
    #         temp.next = head
    #         return temp
    #     else:
    #         return head

    # Iterative
    def swapPairs(self,head):
        # example 1->2->3->4
        result = changing = ListNode(0,head)
        while head and head.next:
            # First Iteration
            temp = head.next    # temp = 2->3->4
            head.next = temp.next   # head = 1->3->4
            temp.next = head    # temp = 2->1->3->4
            head= head.next # head = 3->4
            changing.next = temp    # changing = 0->2->1->3->4
            changing = temp.next    # changing = 3->4
        return result.next
            
        
        