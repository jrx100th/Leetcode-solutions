# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        if head is None:
            return head
        dummy = ListNode(None)
        dummy.next = head
        current = dummy.next
        to_move = current.next

        while current and to_move:

            current.next = to_move.next
            to_move.next = dummy.next
            dummy.next = to_move

            to_move = current.next
        head = dummy.next
        return head