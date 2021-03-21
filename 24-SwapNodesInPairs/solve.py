# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        else:
            tmp = head
            tmp2 = head.next
            head = head.next
            tmp.next = tmp2.next
            tmp2.next = tmp
            last_node = tmp
            tmp = tmp.next

            while tmp and tmp.next:
                tmp2 = tmp.next
                tmp.next = tmp2.next
                last_node.next = tmp2
                tmp2.next = tmp
                last_node = tmp
                tmp = tmp.next
        
        return head
        