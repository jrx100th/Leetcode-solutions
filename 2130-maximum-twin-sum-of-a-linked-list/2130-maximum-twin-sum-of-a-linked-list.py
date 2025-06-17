# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        before = head

        n = 0

        while before is not None:
            n += 1
            before = before.next
        before = head
        for _ in range((n//2)-1):
            before = before.next
        
        temp = before.next
        after = temp.next

        for _ in range(n//2):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

        m = 0

        current = head
        for _ in range(n//2):
            c = current.val + before.val
            if c > m:
                m = c
            current = current.next
            before = before.next
        
        return m
