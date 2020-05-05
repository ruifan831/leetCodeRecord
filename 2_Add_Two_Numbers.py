# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        start_node=ListNode(0)
        changing_node=start_node
        carry_over=0
        while l1 or l2:
            x= l1.val if (l1 is not None) else 0
            y= l2.val if (l2 is not None) else 0
            temp=x+y+carry_over
            l1=l1.next if (l1 is not None) else None
            l2=l2.next if (l2 is not None) else None
            carry_over=temp//10
            changing_node.next=ListNode(temp%10)
            changing_node=changing_node.next
        if carry_over>0:
            changing_node.next=ListNode(carry_over)
        
        return start_node.next
        
            