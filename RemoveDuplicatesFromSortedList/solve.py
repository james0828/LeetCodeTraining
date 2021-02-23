# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        tmp = head
        
        while True:
            if tmp is None or tmp.next is None:
                break
            while tmp.val == tmp.next.val:
                t = tmp.next
                tmp.next = tmp.next.next
                del t
                if tmp.next is None:
                    break
            tmp = tmp.next

        return head
