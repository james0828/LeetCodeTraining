# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length = 0
        t = head
        while t:
            length += 1
            t = t.next
            
        if length == 1:
            return None
        
        if length == n:
            return head.next
        
        t = head
        for i in range(0, length-n-1):
            t = t.next
            length -= 1
        
        l = t.next
        t.next = l.next
        del l
        
        return head