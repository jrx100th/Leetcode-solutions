# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if head is None or k == 1:
            return head

        dummy = ListNode(None)
        prev = dummy
        dummy.next = head

        node = head
        n = 0

        while node:
            n+=1
            node = node.next
        
        while n >= k:
            temp = prev.next
            ntm = temp.next
            for _ in range(k-1):
                temp.next = ntm.next
                ntm.next = prev.next
                prev.next = ntm
                ntm = temp.next

            prev = temp
            n -= k

        return dummy.next