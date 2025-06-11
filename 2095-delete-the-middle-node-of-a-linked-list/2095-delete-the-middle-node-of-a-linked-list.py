# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow = head
        fast = head
        dummy = ListNode(None)
        prev = dummy
        dummy.next = head

        while fast and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            prev = prev.next

        prev.next = slow.next
        slow.next = None

        return dummy.next

        