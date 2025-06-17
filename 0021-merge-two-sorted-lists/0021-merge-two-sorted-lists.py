# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = []

        current = list1

        while current:
            res.append(current.val)
            current = current.next
        
        current = list2

        while current:
            res.append(current.val)
            current = current.next

        res.sort()
        
        reslin = ListNode(None)
        r = reslin

        for num in res:
            reslin.next = ListNode(num)
            reslin = reslin.next

        return r.next