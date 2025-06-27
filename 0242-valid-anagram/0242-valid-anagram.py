class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        # Count characters in s
        for char in s:
            count[char] = count.get(char, 0) + 1

        # Subtract counts using t
        for char in t:
            if char not in count:
                return False
            count[char] -= 1
            if count[char] < 0:
                return False

        # All counts should be zero
        return True
