class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # hint use .count() method

        s = sorted(s)
        t = sorted(t)

        return s==t

        # use hashmap