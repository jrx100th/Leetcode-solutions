# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        result = ListNode(None)
        nh = result
        current = head

        while current is not None:
            if current.val != val:
                result.next = ListNode(current.val)
                result = result.next
            current = current.next

        return nh.next