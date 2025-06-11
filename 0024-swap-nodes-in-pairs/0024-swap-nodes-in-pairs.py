# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None)
        dummy.next = head
        prev = dummy

        while prev.next and prev.next.next:
            n1 = prev.next
            n2 = n1.next

            n1.next = n2.next
            n2.next = prev.next
            prev.next = n2

            prev = n1

        head = dummy.next
        return head