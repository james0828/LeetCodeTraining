# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        tmp = head
        last_node = None
        while tmp:
            print(tmp.val)
            length = 0
            find_next = tmp
            next_last = tmp
            
            try:
                for i in range(k):
                    find_next = find_next.next
            except:
                break

            tmp2 = tmp.next
            tmp.next = find_next
            
            for i in range(k-1):
                tmp3 = tmp2.next
                tmp2.next = tmp
                tmp = tmp2
                tmp2 = tmp3
            
            if last_node:
                last_node.next = tmp
            else:
                head = tmp

            last_node = next_last
            tmp = find_next
            
        return head