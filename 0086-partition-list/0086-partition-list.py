# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """

        dummy1 = ListNode(None)
        dummy2 = ListNode(None)
        tail1 = dummy1
        tail2 = dummy2
        current = head
        while current:
            if current.val < x:
                tail1.next = current
                tail1 = tail1.next
            else:
                tail2.next = current
                tail2 = tail2.next
            current = current.next

        tail2.next = None
        tail1.next = dummy2.next
        head = dummy1.next
        
        return head