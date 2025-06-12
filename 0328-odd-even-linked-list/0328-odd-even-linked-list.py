# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = head

        head1 = ListNode(None)
        head2 = ListNode(None)

        tail1 = head1
        tail2 = head2
        n = 1
        while current:
            if n % 2 == 1:
                tail1.next = current
                tail1 = tail1.next
            else:
                tail2.next = current
                tail2 = tail2.next

            current = current.next
            n+=1

        tail1.next = head2.next
        tail2.next = None
        head = head1.next

        return head