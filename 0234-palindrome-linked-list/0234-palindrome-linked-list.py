# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        if head is None:
            return True
        if head.next is None:
            return True
        else:

            before = head

            n = 0

            while before is not None:
                n += 1
                before = before.next

            before = head

            if n%2 == 0:
                for _ in range((n//2)-1):
                    before = before.next
            else:
                for _ in range((n//2)):
                    before = before.next

            temp = before.next
            after = temp.next

            for _ in range((n//2)):
                after = temp.next
                temp.next = before
                before = temp
                temp = after
            
            # the second half of the list is reversed
            # before is in the tail of the second half of the linked list

            # since the job of after and temp are done, i will use them for another purpose

            temp = head
            after = None

            for _ in range(n//2):
                if temp.val != before.val:
                    return False
                temp, before = temp.next,before.next
            return True