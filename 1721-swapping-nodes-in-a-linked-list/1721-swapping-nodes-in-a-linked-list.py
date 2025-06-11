# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        temp1 = head
        temp2 = head

        for _ in range(k-1):
            temp1 = temp1.next

        n = 0

        trav = temp1

        while trav:
            n+=1
            trav = trav.next

        for _ in range(n-1):
            temp2 = temp2.next

        temp1.val, temp2.val = temp2.val, temp1.val

        return head