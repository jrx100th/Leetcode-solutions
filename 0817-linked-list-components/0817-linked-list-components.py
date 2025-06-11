# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        count = 0
        current = head
        nums = set(nums)
        while current:
            if current.val in nums and (current.next is None or current.next.val not in nums):
                count += 1
            current = current.next
        return count