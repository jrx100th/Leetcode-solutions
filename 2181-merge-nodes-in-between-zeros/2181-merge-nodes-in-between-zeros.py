# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dummy = ListNode(None)
        dummy.next = head

        result = ListNode(None)
        rh = result

        current = dummy.next
        current = current.next

        temp = 0

        # return current.val

        while current.next is not None:
            temp += current.val
            current = current.next
            if current.val == 0:
                result.next = ListNode(temp)
                result = result.next
                temp = 0

        return rh.next