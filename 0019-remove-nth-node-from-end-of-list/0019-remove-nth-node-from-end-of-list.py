# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(None)
        dummy.next = head

        current = dummy
        for _ in range(n):
            current = current.next
        
        
        m = 0

        while current:
            m+=1
            current = current.next
        prev = dummy

        for _ in range(m-1):
            prev = prev.next
        current = prev.next

        prev.next = current.next
        current.next = None

        return dummy.next

        