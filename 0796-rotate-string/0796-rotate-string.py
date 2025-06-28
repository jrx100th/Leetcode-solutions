class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        from collections import deque

        if len(s) != len(goal) or len(set(s)) != len(set(goal)):
            return False

        s = deque(s)
        x = s
        for i in range(len(s)):
            x.rotate(-1)
            if "".join(x) == goal:
                return True
        return False
            
        