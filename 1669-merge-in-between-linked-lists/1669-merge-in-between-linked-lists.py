# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:

        tail2 = list2
        while tail2.next:
            tail2 = tail2.next

        prev1 = list1
        for _ in range(a-1):
            prev1 = prev1.next
        
        prev2 = list1
        for _ in range(b):
            prev2 = prev2.next

        after = list1
        for _ in range(b+1):
            after = after.next

        prev1.next = list2
        tail2.next = after
        prev2.next = None

        return list1