# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head.next is None:
            return head

        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a

        prev = head
        current = prev.next

        while prev and current:

            new = ListNode(gcd(prev.val, current.val))

            prev.next = new
            new.next = current

            prev = current
            current = current.next

        return head
