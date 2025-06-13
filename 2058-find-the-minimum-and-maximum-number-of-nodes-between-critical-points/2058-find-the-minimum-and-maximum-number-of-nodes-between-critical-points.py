# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        
        cp = []
        n = 1
        prev = head
        current = prev.next
        while current.next:

            # minima
            if prev.val > current.val < current.next.val:
                cp.append(n)
            # maxima
            if prev.val < current.val > current.next.val:
                cp.append(n)

            n+=1
            prev = prev.next
            current = prev.next

        if len(cp) < 2:
            return [-1,-1]
        
        cp.sort()

        maxi = abs(max(cp)-min(cp))
        
        mini = 100000
        x = 0
        for i in range(len(cp)-1):
            x = cp[i+1]-cp[i]
            if x < mini:
                mini = x

        return [mini,maxi]
