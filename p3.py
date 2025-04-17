# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None
        next = None
        while cur != None:
            next = cur.next

            cur.next = prev

            prev = cur
            cur = next

        return prev
    
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        elif head.next == None:
            return head
        else:
            tail = self.reverseList(head.next)
            head.next.next = head
            head.next = None
            return tail
            

            