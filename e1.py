# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        a1 = 0
        a2 = 0
        t3 = 0 
        while l1 != None or l2 != None:
            a1 = l1.val if l1 != None else 0
            a2 = l2.val if l2 != None else 0
            t3 = a1+a2
            if t3 