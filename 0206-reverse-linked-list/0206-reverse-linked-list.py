# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return None
        dummy = ListNode(None)

        dummy.next = head
        prev = dummy
        n1 = prev.next
        n2 = n1.next

        while n1 and n2:

            n1.next = n2.next
            n2.next = prev.next
            prev.next = n2

            n2 = n1.next
            

        return dummy.next
