class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        
        if len(set(s)) != len(set(goal)) or len(s) != len(goal):
            return False

        s = s+s
        return goal in s