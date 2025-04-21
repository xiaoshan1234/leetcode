# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode],cur: Optional[ListNode],k:int):
        for _ in range(k):
            nextNode=head.next
            head.next=cur
            cur=head
            head=nextNode
        return cur
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cnt=0
        Fast=head
        while Fast and cnt<k:
            cnt+=1
            Fast=Fast.next
        if cnt==k:
            Fast=self.reverseKGroup(Fast,k)
            head=self.reverseList(head,Fast,k)
        return head