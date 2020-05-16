# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        final_result = ListNode(0)
        changing_node = final_result
        while l1 and l2:
            if l1.val < l2.val:
                changing_node.next = l1
                changing_node = changing_node.next
                l1 = l1.next
            else:
                changing_node.next = l2
                changing_node = changing_node.next
                l2 = l2.next
        if l1:
            changing_node.next = l1
        else:
            changing_node.next = l2
        return final_result.next