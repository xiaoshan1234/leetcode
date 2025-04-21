# Definition for singly-linked list.
from typing import *
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        prev = None
        rst = n0 = ListNode(next=head) # n0 空头节点
        n=0
        while cur != None:
            cur=cur.next
            n+=1
        cur=head
        while n>=k:
            n-=k
            for i in range(k):
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next

            n1 = n0.next # 取头部
            n1.next = cur # 头变尾,接后面
            n0.next = prev # 尾变头，接前面
            n0 = n1 # 下段的空头节点为n1
        
        return rst.next
            