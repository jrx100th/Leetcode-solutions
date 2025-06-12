# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        """
        current = head
        nums = set(nums)
       
        result = ListNode(None)
        res = result

        while current:
            if current.val not in nums:
                result.next = ListNode(current.val)
                result = result.next
            current = current.next

        return res.next
"""     # this is a good but not the optimal approach

        nums = set(nums)

        dummy = ListNode()
        
        dummy.next = head

        current, prev = head, dummy


        while current:
            if current.val in nums:
                prev.next = current.next
            else:
                prev = current
            current = current.next

        return dummy.next