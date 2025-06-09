# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        
        # this is a 1 based indexing
        # so check when you write for it
        # as you worked previously with the 0 based indexing lL

        dummy = ListNode(None)
        prev = dummy
        dummy.next = head

        for _ in range(left-1):
            prev = prev.next

        current = prev.next
        to_move = current.next

        for _ in range(right-left):
            
            current.next = to_move.next
            to_move.next = prev.next
            prev.next = to_move

            to_move = current.next

        head = dummy.next

        return head