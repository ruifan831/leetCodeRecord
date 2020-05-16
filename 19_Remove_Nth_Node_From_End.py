# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        new_node = ListNode(0,head)
        first_pointer = new_node
        second_pointer = new_node
        for i in range(n+1):
            first_pointer = first_pointer.next
        while first_pointer:
            first_pointer = first_pointer.next
            second_pointer = second_pointer.next
        print(second_pointer)
        second_pointer.next = second_pointer.next.next
        return new_node.next